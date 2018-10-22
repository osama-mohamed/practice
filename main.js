const CLIENTID = '7c80255428a2c94ac7ab';
const CLIENTSECRET = '0d21bf38b2edcbec8e9314abc6026284ff6d9127';


$(document).ready(() => {
  $('html').on('click', '#osamaMohamed', (e) => {
    const username = e.target.dataset.name;
    $("#searchUser").val(username);
    $appendRepositories(username);
    $("#search-repository").on("keyup", event => {
      $appendSearchRepository(event, username);
    });
  });
  $('html').on('click', '.repository-name', (e) => {
    $("#search-repository").val(e.target.dataset.name);
    e.target.value = e.target.dataset.name;
    $appendSearchRepository(e, e.target.dataset.owner);
  });

  $("#searchUser").on("keyup", event => {
    $("#search-repository").on("keyup", e => {
      $appendSearchRepository(e, event.target.value);
    });
    $appendRepositories(event.target.value);
  });
  
  $('html').on('click', '.clone', (e) =>{
    cloneRepository(e);
  });
});

function cloneRepository(e) {
  e.preventDefault();
  const tooltip = e.target.children[0];
  // tooltip.innerHTML = "Copied: git clone " + e.target.href;
  tooltip.innerHTML = "&check; &ensp; Coppied to clipboard";
  copy('git clone ' + e.target.href);
  setTimeout(() => {
    e.target.children[0].innerHTML = "Copy to clipboard";
  }, 1000);
}


function copy(text) {
  let copyText = document.createElement("textarea");
  document.body.appendChild(copyText);
  copyText.value = text;
  console.log(copyText.value);
  copyText.select();
  document.execCommand("copy");
  document.body.removeChild(copyText);
}


function $appendSearchRepository(e, username) {
  const searchRepository = e.target.value;
  $('#searched-repository').html('');
  $.ajax({
    url: `https://api.github.com/repos/${username}/${searchRepository}`,
    method: "GET",
    data: {
        client_id: CLIENTID,
        client_secret: CLIENTSECRET
    }
  }).done(repository => {
    if(repository.forks_count > 0){
      // make ajax to get forks details
      $.ajax({
        url: repository.forks_url,
        method: "GET",
        data: {
          client_id: CLIENTID,
          client_secret: CLIENTSECRET,
        }
      }).done(forks => {
        // append searched repo with forks
        repositoryWithForks('#searched-repository', repository, null, forks);
      });
    } else {
      // append searched repo with 0 forks  
      // this method(repositoryWithForks) requires this ==> (htmlTage to append to, repository, index, forks)
      repositoryWithForks('#searched-repository', repository);
    }
  });
}


function $appendRepositories(username) {
  $.ajax({
    url: `https://api.github.com/users/${username}`,
    method: "GET",
    data: {
        client_id: CLIENTID,
        client_secret: CLIENTSECRET
    }
  }).done(user => {
    $.ajax({
      url: `https://api.github.com/users/${username}/repos`,
      method: "GET",
      data: {
        client_id: CLIENTID,
        client_secret: CLIENTSECRET,
        sort: 'pushed',
        // sort: 'created',
        // direction: 'asc',
        per_page: 5000
      }
    }).done(repositories => {
      // loop to append repos details
      $.each(repositories, (index, repository)=> {
        if(repository.forks_count > 0){
          // make ajax to get forks details
          $.ajax({
            url: repository.forks_url,
            method: "GET",
            data: {
              client_id: CLIENTID,
              client_secret: CLIENTSECRET,
            }
          }).done(forks => {
            // append repos with forks
            repositoryWithForks('#repositories', repository, index, forks);
          });
        } else {
          // append repos with 0 forks
          repositoryWithForks('#repositories', repository, index);
        }
      });
    });
    // append user profile details
    userProfile("#profile", user, username);
  })
  .fail(err => {
    $("#profile").text(`User ${username} ${JSON.parse(err.responseText).message}`);
  }); 
}


function userProfile(html, user, username) {
  $(html).html(`
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title">${user.name || user.login}</h3>
      </div>
      <div class="panel-body">
        <div class="row">
          <div class="col-md-3">
          <a href="${user.avatar_url}" target="_blank">
            <img class="thumbnail avatar" src="${user.avatar_url}" title="${user.name}" alt="${user.name}">
          </a>
            <a href="${user.html_url}" target="_blank" class="btn btn-info btn-block">Go to ${user.name || user.login} Profile</a>
            <br>
            <a href="https://gist.github.com/${username}" target="_blank" class="btn btn-warning btn-block">Go to ${user.name || user.login} Gists Page</a>
            </div>
            <div class="col-md-9">
            <span class="label label-info">Public Repositories: ${user.public_repos}</span>
            <span class="label label-warning">Public Gists: ${user.public_gists}</span>
            <span class="label label-success">Followers: ${user.followers}</span>
            <span class="label label-danger">Following: ${user.following}</span>
            <br>
            <br>
            <ul class="list-group">
              <li class="list-group-item">ID: ${user.id}</li>
              <li class="list-group-item">Company: ${user.company}</li>
              <li class="list-group-item">Website: <a href="${user.blog}" target="_blank" class="user-website">${user.blog}</a></li>
              <li class="list-group-item">email: ${user.email}</li>
              <li class="list-group-item">Location: ${user.location}</li>
              <li class="list-group-item">Member Since: ${user.created_at}</li>
              <li class="list-group-item">Bio: ${user.bio}</li>
              <li class="list-group-item">Hireable: <input type="checkbox" checked="${user.hireable}" disabled="${true}"></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  `);
  if(user.public_repos) {
    $(html).append(`<h3 class="page-header">Latest Repositories</h3>
    <div id="repositories"></div>`);
  }
}


function repositoryWithForks(html, repository, index, forks) {
  $('#repositoriesButtons').append(
    `<div class="col-md-3">
      <a data-name="${repository.name}" data-owner="${repository.owner.login}" href="${repository.html_url}" target="_blank" class="btn btn-info repository-name">${repository.name}</a>
    </div>`);
  let license = '';
  if(repository.license) {
    license += `
    <a href="${repository.license.url}" target="_blank" class="license-url">
      <span class="label label-default">License: ${repository.license.spdx_id}</span>
    </a>`;
  }
  let forksNames = '';
  let text = '';
  let repositoryIndex = '';
  let forksRepositoryIndex = '';
  if(forks) {
    text = `&emsp; <strong>Forks from: `;
    for(let i = 0; i < forks.length; i++) {
      forksNames += `<a href="${forks[i].owner.html_url}" target="_blank" class="repo-name">${forks[i].owner.login}</a>, `;
    }
    if(index || index == 0) {
      forksRepositoryIndex = `##${index + 1}`;
    }
  } else {
    if(index || index == 0) {
      repositoryIndex = `#${index + 1}`;
    }
  }
  $(html).append(`
    <div class="well">
      <div class="row">
        <div class="col-md-6">` +
          repositoryIndex +
          forksRepositoryIndex +
          `
          <br>
          <strong>Repository ID : ${repository.id}</strong>
          <br>
          <strong>Repository Name: <a href="${repository.html_url}" target="_blank" class="repo-name">${repository.name}</a></strong>
          <br> 
          <p><strong>Repository Description : </strong>${repository.description}</p>
        </div>
        <div class="col-md-4">
          <span class="label label-info">Forks: ${repository.forks_count}</span>
          <span class="label label-warning">Watchers: ${repository.watchers_count}</span>
          <span class="label label-success">Stars: ${repository.stargazers_count}</span>
          <span class="label label-primary">Open Issues: ${repository.open_issues_count}</span>
          <br>
          <br>` +
          license +
          text +
          forksNames +
          `
          </strong>
        </div>
        <div class="col-md-2">
          <span class="tooltipp">
            <a href="${repository.clone_url}" class="btn btn-info btn-block clone">Clone Repo
              <span class="tooltiptext">Copy to clipboard</span>
            </a>
          </span>
          <a href="${repository.svn_url}/archive/master.zip" target="_blank" class="btn btn-success btn-block" style="margin-top: 10px; margin-bottom: 10px;">Download ZIP</a>
          <a href="${repository.homepage}" target="_blank" class="btn btn-warning btn-block">Home Page</a>
        </div>
      </div>
    </div>
  `);
}


function gitStatus() {copy('git status');}

function gitAddAll() {copy('git add .');}

function gitCommit(text) {copy(text + ' ""');}

function gitPush() {copy('git push');}

function gitPushUOriginMaster() {copy('git push -u origin master');}

function gitReset() {copy('git reset --hard ');}

function gitClean() {copy('git clean -f -d');}

function gitPushUOriginMasterHard() {copy('git push -u origin +master');}

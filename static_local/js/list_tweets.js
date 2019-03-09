function getParameterByName(name, url) {
  if (!url) {
    url = window.location.href;
  }
  name = name.replace(/[\[\]]/g, "\\$&");
  const regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

// function formatTweet(tweetValue) {

//   let preContent;
//   let container;
//   let tweetContent;
//   const isReply = tweetValue.reply;
//   if (tweetValue.parent && !isReply) {
//     tweetValue = tweetValue.parent;
//     preContent = `
//       <span class='grey-color'>
//         Retweet via 
//         <a href="${tweetValue.user.user_url}">${tweetValue.user.username}</a>
//         on ${tweetValue.timesince}
//       </span>
//       <br/>
//       `;
//     } else if (tweetValue.parent && isReply) {
//       preContent = `
//         <span class='grey-color'>
//           Reply to @${tweetValue.parent.user.username}
//         </span>
//         <br/>
//       `;
//     }
//   let verb = 'Like';
//   if (tweetValue.did_like){
//     verb = 'Unlike';
//   }  

//   tweetContent = `
//     <span class='content'>${tweetValue.content}</span>
//     <br/> via 
//     <a href="${tweetValue.user.user_url}">${tweetValue.user.username}</a> | 
//     ${tweetValue.timesince} | 
//     <a href='${tweetValue.view_url}'>View</a> | 
//     <a class='retweetBtn' href='${tweetValue.retweet_url}'>Retweet</a> | 
//     <a href='#' class='tweet-like' data-id="${tweetValue.id}">
//       ${verb} (${tweetValue.likes})
//     </a> | 
//     <a href='#' class='tweet-reply' data-user="${tweetValue.user.username}" data-id="${tweetValue.id}">Reply</a>
//   `;
//   if (preContent){
//     container = `
//       <div class="media">
//         <div class="media-body">
//           ${preContent}
//           ${tweetContent}
//         </div>
//       </div>
//       <hr/>
//     `;
//   } else {
//     container = `
//       <div class="media">
//         <div class="media-body">
//           ${tweetContent}
//         </div>
//       </div>
//       <hr/>
//     `;
//   }
//   return container;
// }

function attachTweet(tweetValue, prepend, retweet){
  const dateDisplay = tweetValue.timesince; // tweetValue.date_display;
  const tweetContent = tweetValue.content;
  const tweetUser = tweetValue.user;
  const isRetweet = tweetValue.is_retweet;
  const isReply = tweetValue.reply;
  let tweetFormattedHtml;
  let owner = '';
  if(tweetValue.owner) {
    owner += `
          |  <a href="${tweetValue.update_url}">Update</a> |
             <a href="${tweetValue.delete_url}">Delete</a>
    `;
  }
  let verb = 'Like';
  if (tweetValue.did_like){
    verb = 'Unlike';
  }
  let replyId = tweetValue.id;
  if (tweetValue.parent) {
    replyId = tweetValue.parent.id;
  }
  let openingContainerDiv = `<div class="media">`;
  if (tweetValue.id == fetchOne) {
    openingContainerDiv = `<div class="media media-focus">`;
    setTimeout(function(){
      $('.media-focus').css("background-color", '#fff');
    }, 2000);
  }
  if (retweet && tweetValue.parent && !isReply){
    const mainTweet = tweetValue.parent;
    tweetFormattedHtml = `
      ${openingContainerDiv}
        <div class="media-body">
          <span class='grey-color'>
            Retweet via <a href='${tweetUser.user_url}'>${tweetUser.username}</a> on ${dateDisplay}
          </span>
          <br/>
          ${mainTweet.content} 
          <br/> 
          via <a href='${mainTweet.user.user_url}'>${mainTweet.user.username}</a> |
          ${mainTweet.timesince} |
          <a href='${mainTweet.view_url}'>View</a> |
          <a href="${mainTweet.retweet_url}" class="retweetBtn" data-href="${mainTweet.api_retweet_url}">Retweet</a> |
          <a href='#' class='tweet-like' data-id=${tweetValue.id}>${verb} (${tweetValue.likes})</a> | 
          <a href='#' class='tweet-reply' data-user="${mainTweet.user.username}" data-id="${replyId}">Reply</a>
        </div>
      </div>
      <hr/>
    `;
    } else if (tweetValue.parent && isReply) {
    tweetFormattedHtml = `
      ${openingContainerDiv}
        <div class="media-body">
          <span class='grey-color'>
            Reply to @${tweetValue.parent.user.username}
          </span>
          <br/>
          ${tweetValue.content} 
          <br/> 
          via <a href='${tweetValue.user.user_url}'>${tweetValue.user.username}</a> |
          ${tweetValue.timesince} |
          <a href='${tweetValue.view_url}'>View</a> |
          <a href="${tweetValue.retweet_url}" class="retweetBtn" data-href="${tweetValue.api_retweet_url}">Retweet</a> |
          <a href='#' class='tweet-like' data-id=${tweetValue.id}>${verb} (${tweetValue.likes})</a> | 
          <a href='#' class='tweet-reply' data-user="${tweetValue.user.username}" data-id="${replyId}">Reply</a>
        </div>
      </div>
      <hr/>
    `;
  } else {
    tweetFormattedHtml = `
      ${openingContainerDiv}
        <div class="media-body">
          ${tweetContent} 
          <br/> 
          via <a href='${tweetUser.user_url}'>${tweetUser.username}</a> |
          ${dateDisplay} | 
          <a href='${tweetValue.view_url}'>View</a> |
          <a href="${tweetValue.retweet_url}" class="retweetBtn" data-href="${tweetValue.api_retweet_url}">Retweet</a> |
          <a href='#' class='tweet-like' data-id=${tweetValue.id}>${verb} (${tweetValue.likes})</a> | 
          <a href='#' class='tweet-reply' data-user="${tweetValue.user.username}" data-id="${replyId}">Reply</a>
          ` + owner +
          ` 
        </div>
      </div>
      <hr/>
    `;
  }
  // tweetFormattedHtml = formatTweet(tweetValue);
  if (prepend == true){
    $("#tweet-container").prepend(tweetFormattedHtml);
  } else {
    $("#tweet-container").append(tweetFormattedHtml);
 }
} 

function parseTweets(tweetList){
  if (tweetList == 0) {
    $("#tweet-container").text("No tweets currently found.");
  } else {
    $.each(tweetList, function(key, value){
      if (value.parent) {
        attachTweet(value, false, true);
      } else {
        attachTweet(value);
      }
    });
  }
}

function fetchTweets(url){
  const query = getParameterByName('q');
  let tweetList = [];
  let fecthUrl;
  if (!url) {
    fecthUrl = $("#tweet-container").attr("data-url") || "/api/tweet/";
  } else {
    fecthUrl = url;
  }
  $.ajax({
    url: fecthUrl,
    data: {
      "q": query
    },
    method: "GET",
    success: function(data){
      tweetList = data.results;
      if (data.next){
        nextTweetUrl = data.next;
      } else {
        $("#loadmore").css("display", "none");
      }
      parseTweets(tweetList);
      updateHashLinks();
    },
    error: function(error){
      console.log("error while listing tweets", error);
    }
  });
}

function updateHashLinks(){
  $(".media-body").each(function(data){
    const hashtagRegex = /(^|\s)#([\w\d-]+)/g;
    const usernameRegex = /(^|\s)@([\w\d-]+)/g;
    const currentHtml = $(this).html();
    let newText;
    newText = currentHtml.replace(hashtagRegex, "$1<a href='/tags/$2/'>#$2</a>");
    newText = newText.replace(usernameRegex, "$1 @<a href='/$2/'>$2</a>");
    $(this).html(newText);
  });
}

let nextTweetUrl;


function loadTweetData () {
  fetchTweets();
  let charsStart = 140;
  let charsCurrent = 0;
  $(".tweet-form").append(`<span class='tweetCharsLeft' style='margin-left: 20px'>${charsStart} left</span>`);
  $(".tweet-form textarea").keyup(function(event){
    const tweetValue = $(this).val();
    charsCurrent = charsStart - tweetValue.length;
    const spanChars = $(this).parent().parent().parent().find("span.tweetCharsLeft");
    spanChars.text(charsCurrent);
    if (charsCurrent > 0 ) {
      spanChars.removeClass("grey-color").removeClass("red-color");
    } else if (charsCurrent == 0) {
      spanChars.removeClass("red-color").addClass("grey-color");
    } else if (charsCurrent < 0) {
      spanChars.removeClass("grey-color").addClass("red-color");
    }
  });

  $(".tweet-form").submit(function(event){
    event.preventDefault();
    const this_ = $(this);
    const formData =  this_.serialize();
    if (charsCurrent >= 0) {
      $.ajax({
        url: "/api/tweet/create/",
        data: formData,
        method: "POST",
        success: function(data){
          // this_[0].reset();
          this_.find("input[type=text], textarea").val("");
          attachTweet(data, true);
          updateHashLinks();
          $("#replyModal").modal("hide");
          charsStart = 140;
        },
        error: function(error){
          console.log("error while submitting new tweet ", error, error.statusText, error.status);
        }
      });
    }  else {
      console.log("Cannot send, tweet too long.");
      alert("Cannot send, tweet too long.");
    }
  });

  $("#loadmore").click(function(event){
    event.preventDefault();
    if (nextTweetUrl) {
      fetchTweets(nextTweetUrl);
    }
  });  
}

$(document.body).on("click", ".retweetBtn", function(e){
  e.preventDefault();
  let url = $(this).attr('data-href');
  $.ajax({
    method: "GET",
    url: url,
    success: function (data) {
      if ($("#tweet-container").attr("data-url") == "/api/tweet/") {
        attachTweet(data, true, true);
        updateHashLinks();
      }
    },
    error: function(error){
      console.log("error while retweet ", error);
    }
  });
});

$(document.body).on("click", ".tweet-like", function(e){
  e.preventDefault();
  const this_ = $(this);
  const tweetId = this_.attr("data-id");
  const likedUrl = `/api/tweet/${tweetId}/like/`;
  $.ajax({
    method:"GET",
    url: likedUrl,
    success: function(data){
      if (data.liked){
        this_.text("Like");
      } else {
        this_.text("Unlike");
      }
    },
    error: function(error){
      console.log("error while like tweet ", error);
    }
  });
});

$(document.body).on("click", ".tweet-reply", function(e){
  e.preventDefault();
  const this_ = $(this);
  const parentId = this_.attr("data-id");
  const username = this_.attr("data-user");
  const content = this_.parent().parent().find(".content").text();
  $("#replyModal").modal({});
  $("#replyModal textarea").after(`<input type='hidden' value='${parentId}' name='parent_id'/>`);
  $("#replyModal textarea").after(`<input type='hidden' value='${true}' name='reply'/>`);
  $("#replyModal textarea").val("@" + username + " ");
  $("#replyModal #replyModalLabel").text("Reply to " + content);
  // charsStart = 140;
  // charsStart = charsStart - $("#replyModal textarea").val().length;
  // $(".tweet-form span.tweetCharsLeft").remove();
  // $(".tweet-form").append(`<span class='tweetCharsLeft'>${charsStart}</span>`);
  $("#replyModal").on("shown.bs.modal", function(){
    $('textarea').focus();
  });
});

// $(document).ready(() => {
//   loadTweetData();
// });
let fetchOne;
function fetchSingle(fetchOneId){
  fetchOne = fetchOneId;
  const fecthDetailUrl = `/api/tweet/${fetchOneId}/`;
  $.ajax({
    url: fecthDetailUrl,
    method: "GET",
    success: function(data){
      tweetList = data.results;
      parseTweets(tweetList);
      updateHashLinks();
    },
    error: function(error){
      console.log("error while fetching single tweet detail ", error);
    }
  });
}

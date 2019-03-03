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

function attachTweet(tweetValue, prepend, retweet){
  const dateDisplay = tweetValue.timesince; // tweetValue.date_display;
  const tweetContent = tweetValue.content;
  const tweetUser = tweetValue.user;
  const isRetweet = tweetValue.is_retweet;
  let owner = '';
  if(tweetValue.owner) {
    owner += `
          |  <a href="${tweetValue.update_url}">Update</a> |
             <a href="${tweetValue.delete_url}">Delete</a>
    `;
  }
  let tweetFormattedHtml;
  if (retweet && tweetValue.parent){
    const mainTweet = tweetValue.parent;
    tweetFormattedHtml = `
      <div class="media">
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
          <a href="${mainTweet.retweet_url}" class="retweetBtn" data-href="${mainTweet.api_retweet_url}">Retweet</a>
        </div>
      </div>
      <hr/>
    `;
  } else {
    tweetFormattedHtml = `
      <div class="media">
        <div class="media-body">
          ${tweetContent} 
          <br/> 
          via <a href='${tweetUser.user_url}'>${tweetUser.username}</a> |
          ${dateDisplay} | 
          <a href='${tweetValue.view_url}'>View</a> |
          <a href="${tweetValue.retweet_url}" class="retweetBtn" data-href="${tweetValue.api_retweet_url}">Retweet</a>
          ` + owner +
          ` 
        </div>
      </div>
      <hr/>
    `;
  }
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
    fecthUrl = "/api/tweet/";
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
    let newText = $(this).html().replace(hashtagRegex, "$1<a href='/tags/$2/'>#$2</a>");
    $(this).html(newText);
  });
}

let nextTweetUrl;

$(document).ready(() => {
  fetchTweets();
    
  const charsStart = 140;
  let charsCurrent = 0;
  $("#tweet-form").append(`<span id='tweetCharsLeft'>${charsStart}</span>`);
  $("#tweet-form textarea").keyup(function(event){
    const tweetValue = $(this).val();
    charsCurrent = charsStart - tweetValue.length;
    const spanChars = $("#tweetCharsLeft");
    spanChars.text(charsCurrent);
    if (charsCurrent > 0 ) {
      spanChars.removeClass("grey-color").removeClass("red-color");
    } else if (charsCurrent == 0) {
      spanChars.removeClass("red-color").addClass("grey-color");
    } else if (charsCurrent < 0) {
      spanChars.removeClass("grey-color").addClass("red-color");
    }
  });

  $("#tweet-form").submit(function(event){
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

  $(document.body).on("click", ".retweetBtn", function(e){
    e.preventDefault();
    let url = $(this).attr('data-href');
    $.ajax({
      method: "GET",
      url: url,
      success: function (data) {
        attachTweet(data, true, true);
        updateHashLinks();
      },
      error: function(error){
        console.log("error while retweet ", error);
      }
    });
  });

});

webpackJsonp([3],{NNcU:function(t,a,e){(t.exports=e("FZ+f")(!1)).push([t.i,".post-thumbnail[data-v-08baa45c]{width:100%;height:300px;background-size:cover;background-position:50%}.post-content[data-v-08baa45c]{width:80%;max-width:500px;margin:auto}.post-content p[data-v-08baa45c]{white-space:pre-line}",""])},SlRu:function(t,a,e){"use strict";var n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{directives:[{name:"editable",rawName:"v-editable",value:t.blok,expression:"blok"}],attrs:{id:"post"}},[e("div",{staticClass:"post-thumbnail",style:{backgroundImage:"url("+t.image+")"}}),e("section",{staticClass:"post-content"},[e("h2",[t._v(t._s(t.id))]),e("h1",[t._v(t._s(t.title))]),e("p",[t._v(t._s(t.content))]),e("p",[t._v(t._s(t.summary))])])])};n._withStripped=!0;var o={render:n,staticRenderFns:[]};a.a=o},e8Dn:function(t,a,e){var n=e("NNcU");"string"==typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);e("rjj0")("82593e68",n,!1,{sourceMap:!1})},h61i:function(t,a,e){"use strict";a.a={asyncData:function(t){return t.app.$storyapi.get("cdn/stories/blog/"+t.params.postId,{version:"published"}).then(function(t){return{blok:t.data.story,id:t.data.story.id,title:t.data.story.content.title,content:t.data.story.content.content,summary:t.data.story.content.summary,image:t.data.story.content.thumbnail}})},mounted:function(){this.$storyblok.init(),this.$storyblok.on("change",function(){location.reload(!0)})}}},pA05:function(t,a,e){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var n=e("h61i"),o=e("SlRu"),s=!1;var i=function(t){s||e("e8Dn")},r=e("VU/8")(n.a,o.a,!1,i,"data-v-08baa45c",null);r.options.__file="pages\\blog\\_postId\\index.vue",a.default=r.exports}});
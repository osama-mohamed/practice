webpackJsonp([1],{"3v7I":function(t,e,i){var r=i("KpxJ");"string"==typeof r&&(r=[[t.i,r,""]]),r.locals&&(t.exports=r.locals);i("rjj0")("79ce60a5",r,!1,{sourceMap:!1})},DUcc:function(t,e,i){"use strict";var r=i("DvXb");e.a={components:{PostPreview:r.a},asyncData:function(t){return t.app.$storyapi.get("cdn/stories",{version:t.isDev?"draft":"published",starts_with:"blog/"}).then(function(t){return{posts:t.data.stories.map(function(t){return{id:t.slug,title:t.content.title,previewText:t.content.summary,thumbnailUrl:t.content.thumbnail}})}})}}},DvXb:function(t,e,i){"use strict";var r=i("eWcu"),n=i("UADX"),a=!1;var o=function(t){a||i("SXXc")},s=i("VU/8")(r.a,n.a,!1,o,"data-v-53df47b6",null);s.options.__file="components\\Blog\\PostPreview.vue",e.a=s.exports},I17g:function(t,e,i){(t.exports=i("FZ+f")(!1)).push([t.i,"a[data-v-53df47b6]{text-decoration:none;color:#000}.post-preview[data-v-53df47b6]{border-radius:3px;-webkit-box-shadow:1px 1px 5px 1px rgba(0,0,0,.5);box-shadow:1px 1px 5px 1px rgba(0,0,0,.5);width:90%;height:320px;height:20rem;margin:16px;margin:1rem}.post-preview-thumbnail[data-v-53df47b6]{background-position:50%;background-size:cover;width:100%;height:160px;height:10rem}.post-preview-content[data-v-53df47b6]{text-align:center;padding:16px;padding:1rem}@media (min-width:35rem){.post-preview[data-v-53df47b6]{width:25rem}}",""])},KpxJ:function(t,e,i){(t.exports=i("FZ+f")(!1)).push([t.i,"#posts[data-v-dba527ce]{padding-top:32px;padding-top:2rem;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}@media (min-width:55rem){#posts[data-v-dba527ce]{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}}",""])},SXXc:function(t,e,i){var r=i("I17g");"string"==typeof r&&(r=[[t.i,r,""]]),r.locals&&(t.exports=r.locals);i("rjj0")("d3a61214",r,!1,{sourceMap:!1})},UADX:function(t,e,i){"use strict";var r=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("section",{staticClass:"container"},[i("nuxt-link",{attrs:{to:t.id}},[i("article",{staticClass:"post-preview"},[i("div",{staticClass:"post-preview-thumbnail",style:{backgroundImage:"url("+t.thumbnailImage+")"}}),i("div",{staticClass:"post-preview-content"},[i("h1",[t._v(t._s(t.title))]),i("p",[t._v(t._s(t.excerpt))])])])])],1)};r._withStripped=!0;var n={render:r,staticRenderFns:[]};e.a=n},Y8jH:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=i("DUcc"),n=i("bVkF"),a=!1;var o=function(t){a||i("3v7I")},s=i("VU/8")(r.a,n.a,!1,o,"data-v-dba527ce",null);s.options.__file="pages\\blog_vue_nuxt\\index.vue",e.default=s.exports},bVkF:function(t,e,i){"use strict";var r=function(){var t=this.$createElement,e=this._self._c||t;return e("section",{attrs:{id:"posts"}},this._l(this.posts,function(t){return e("PostPreview",{key:t.id,attrs:{id:"/blog_vue_nuxt/blog/"+t.id,title:t.title,excerpt:t.previewText,thumbnailImage:t.thumbnailUrl}})}))};r._withStripped=!0;var n={render:r,staticRenderFns:[]};e.a=n},eWcu:function(t,e,i){"use strict";e.a={props:{title:{type:String,required:!0},excerpt:{type:String,required:!0},thumbnailImage:{type:String,required:!0},id:{type:String,required:!0}}}}});
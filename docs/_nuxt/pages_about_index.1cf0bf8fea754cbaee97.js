webpackJsonp([4],{VPVA:function(t,e,a){"use strict";var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("section",{directives:[{name:"editable",rawName:"v-editable",value:t.blok,expression:"blok"}],attrs:{id:"about-page"}},[a("h1",[t._v(t._s(t.title))]),a("p",[t._v(t._s(t.content))]),t._m(0),t._m(1),t._m(2),t._m(3)])};i._withStripped=!0;var n={render:i,staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("p",[this._v("E-mail : "),e("a",{attrs:{href:"mailto:osama6osama6@gmail.com"}},[this._v("OSAMA MOHAMED")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("p",[this._v("Github : "),e("a",{attrs:{href:"https://github.com/osama-mohamed",target:"_blank"}},[this._v("OSAMA MOHAMED")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("p",[this._v("Bitbucket : "),e("a",{attrs:{href:"https://bitbucket.org/osama-mohamed",target:"_blank"}},[this._v("OSAMA MOHAMED")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("p",[this._v("Facebook : "),e("a",{attrs:{href:"https://www.facebook.com/osama.mohamed.ms",target:"_blank"}},[this._v("OSAMA MOHAMED")])])}]};e.a=n},Yhi0:function(t,e,a){var i=a("jW9E");"string"==typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);a("rjj0")("fc12be5a",i,!1,{sourceMap:!1})},firx:function(t,e,a){"use strict";e.a={asyncData:function(t){return t.app.$storyapi.get("cdn/stories/about",{version:t.isDev?"draft":"published"}).then(function(t){return{blok:t.data.story.content,title:t.data.story.content.title,content:t.data.story.content.content}})},mounted:function(){this.$storyblok.init(),this.$storyblok.on("change",function(){location.reload(!0)})}}},jW9E:function(t,e,a){(t.exports=a("FZ+f")(!1)).push([t.i,"#about-page[data-v-6de0ee8d]{width:80%;max-width:500px;margin:auto}#about-page p[data-v-6de0ee8d]{white-space:pre-line}",""])},yPeL:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=a("firx"),n=a("VPVA"),s=!1;var o=function(t){s||a("Yhi0")},r=a("VU/8")(i.a,n.a,!1,o,"data-v-6de0ee8d",null);r.options.__file="pages\\about\\index.vue",e.default=r.exports}});
webpackJsonp([4],{"0MkX":function(t,e,n){"use strict";e.a={asyncData:function(t){return t.app.$storyapi.get("cdn/stories/about",{version:t.isDev?"draft":"published"}).then(function(t){return{blok:t.data.story.content,title:t.data.story.content.title,content:t.data.story.content.content}})},mounted:function(){this.$storyblok.init(),this.$storyblok.on("change",function(){location.reload(!0)})}}},"3tEX":function(t,e,n){var a=n("zzs3");"string"==typeof a&&(a=[[t.i,a,""]]),a.locals&&(t.exports=a.locals);n("rjj0")("5cc8f7e5",a,!1,{sourceMap:!1})},VPVA:function(t,e,n){"use strict";var a=function(){var t=this.$createElement,e=this._self._c||t;return e("section",{directives:[{name:"editable",rawName:"v-editable",value:this.blok,expression:"blok"}],attrs:{id:"about-page"}},[e("h1",[this._v(this._s(this.title))]),e("p",[this._v(this._s(this.content))])])};a._withStripped=!0;var i={render:a,staticRenderFns:[]};e.a=i},yPeL:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("0MkX"),i=n("VPVA"),o=!1;var s=function(t){o||n("3tEX")},r=n("VU/8")(a.a,i.a,!1,s,"data-v-6de0ee8d",null);r.options.__file="pages\\about\\index.vue",e.default=r.exports},zzs3:function(t,e,n){(t.exports=n("FZ+f")(!1)).push([t.i,"#about-page[data-v-6de0ee8d]{width:80%;max-width:500px;margin:auto}#about-page p[data-v-6de0ee8d]{white-space:pre-line}",""])}});
<template>
  <div class="header-box">
    <div class="header">
      <div class="content">
        <div class="logo">
          <router-link to="/"><img src="../assets/logo.svg" alt=""></router-link>
        </div>
        <ul class="nav">
          <li><router-link to="">免费课</router-link></li>
          <li><router-link to="">项目课</router-link></li>
          <li><router-link to="">学位课</router-link></li>
          <li><router-link to="">题库</router-link></li>
          <li><router-link to="">路飞学城</router-link></li>
        </ul>
        <div class="search-warp">
          <div class="search-area">
            <input class="search-input" placeholder="请输入关键字..." type="text" autocomplete="off">
            <div class="hotTags">
              <router-link to="/search/?words=Vue" target="_blank" class="">Vue</router-link>
              <router-link to="/search/?words=Python" target="_blank" class="last">Python</router-link>
            </div>
          </div>
          <div class="showhide-search" data-show="no"><img class="imv2-search2" src="../assets/search.svg" /></div>
        </div>
        <div class="login-bar">
          <div class="shop-cart full-left">
            <img src="../assets/cart.svg" alt="" />
            <span><router-link to="/cart">购物车</router-link></span>
          </div>
          <div class="login-box full-left">
            <span>登录</span>
            &nbsp;/&nbsp;
            <span>注册</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.header-box{
  height: 72px;
}
.header{
  width: 100%;
  height: 72px;
  box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  position: fixed;
  top:0;
  left: 0;
  right:0;
  margin: auto;
  z-index: 99;
  background: #fff;
}
.header .content{
  max-width: 1366px;
  width: 100%;
  margin: 0 auto;
}
.header .content .logo{
  height: 72px;
  line-height: 72px;
  margin: 0 20px;
  float: left;
  cursor: pointer;
}
.header .content .logo img{
  vertical-align: middle;
  margin: -40px;
  width: 240px;
}
.header .nav li{
  float: left;
  height: 80px;
  line-height: 80px;
  margin-right: 30px;
  font-size: 16px;
  color: #4a4a4a;
  cursor: pointer;
}
.header .nav li span{
  padding-bottom: 16px;
  padding-left: 5px;
  padding-right: 5px;
}
.header .nav li span a{
  display: inline-block;
}
.header .nav li .this{
  color: #4a4a4a;
  border-bottom: 4px solid #ffc210;
}
.header .nav li:hover span{
  color: #000;
}
.search-warp {
  position: relative;
  float: left;
  margin-left: 24px;
}
.search-warp .showhide-search {
  width: 20px;
  height: 24px;
  text-align: right;
  position: absolute;
  display: inline-block;
  right: 0;
  bottom: 24px;
  padding: 0 8px;
  border-radius: 18px;
}
.search-warp .showhide-search img {
  display: block;
  height: 24px;
  color: #545C63;
  cursor: pointer;
  font-size: 18px;
  line-height: 24px;
  width: 20px;
}
.search-area {
  float: right;
  position: relative;
  height: 40px;
  padding-right: 36px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.4);
  zoom: 1;
  background: #F3F5F6;
  border-radius: 4px;
  margin: 16px 0;
  width: 324px;
  box-sizing: border-box;
  font-size: 0;
  -webkit-transition: width 0.3s;
  -moz-transition: width 0.3s;
  transition: width 0.3s;
}
.search-area .search-input {
  padding: 8px 12px;
  font-size: 14px;
  color: #9199A1;
  line-height: 24px;
  height: 40px;
  width: 100%;
  float: left;
  border: 0;
  -webkit-transition: background-color 0.3s;
  -moz-transition: background-color 0.3s;
  transition: background-color 0.3s;
  background-color: transparent;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -ms-box-sizing: border-box;
  box-sizing: border-box;
}
.search-area .search-input.w100 {
  width: 100%;
}
.search-area .hotTags {
  display: inline-block;
  position: absolute;
  top: 0;
  right: 32px;
}
.search-area .hotTags a {
  display: inline-block;
  padding: 4px 8px;
  height: 16px;
  font-size: 14px;
  color: #9199A1;
  line-height: 16px;
  margin-top: 8px;
  max-width: 60px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.search-area .hotTags a:hover {
  color: #F21F1F;
}
.search-area input::-webkit-input-placeholder {
  color: #9199A1;
}
.search-area input:-moz-placeholder {
  color: #9199A1;
}
.search-area input::-moz-placeholder {
  color: #9199A1;
}
.search-area input:-ms-input-placeholder {
  color: #9199A1;
}
.search-area-result {
  position: absolute;
  left: 0;
  top: 47px;
  width: 324px;
  background-color: #fff;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  border-radius: 0 0 8px 8px;
  z-index: 999;
}
.search-area-result.hot-hide {
  border-top-right-radius: 8px;
  border-top-left-radius: 8px;
  top: 47px;
}
.search-area-result.hot-hide .history {
  border-top: 0;
}
.search-area-result h2 {
  font-size: 12px;
  color: #1C1F21;
  line-height: 12px;
  padding: 12px;
  font-weight: 700;
}
.search-area-result .hot {
  padding: 0 12px 12px;
}
.search-area-result .hot .hot-item {
  background: rgba(84, 92, 99, 0.1);
  border-radius: 12px;
  padding: 4px 12px;
  line-height: 16px;
  margin-right: 4px;
  margin-bottom: 4px;
  display: inline-block;
  cursor: pointer;
  font-size: 12px;
  color: #545C63;
}
.login-bar {
  float: right;
  display: flex;         /* 开启弹性布局，强制子元素在同一行 */
  align-items: center;   /* 强制子元素垂直居中绝对对齐 */
  height: 72px;          /* 让父容器和整个导航栏一样高 */
}
.login-bar .shop-cart {
  margin-right: 20px;
  border-radius: 17px;
  background: #F3F5F6;
  width: 100px;
  height: 34px;
  line-height: 34px;
  text-align: center;
  cursor: pointer;
  /* 删除了容易捣乱的 margin-top，交由 flex 自动居中 */
}
.login-bar .shop-cart:hover {
  color: #000;
}
.login-bar .shop-cart img {
  width: 16px;
  height: 16px;
  vertical-align: middle;
  margin-right: 5px;
}
.login-bar .shop-cart span {
  font-size: 14px;
  color: #4a4a4a;
}
.login-bar .login-box {
  /* 删除了容易捣乱的 margin-top，交由 flex 自动居中 */
}
.login-bar .login-box span {
  color: #4a4a4a;
  cursor: pointer;
}
.login-bar .login-box span:hover {
  color: #000;
}
</style>
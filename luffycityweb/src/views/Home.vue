<template>
  <div class="home">
    <Header></Header>
    <Footer></Footer>
  </div>

</template>

<script setup>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import axios from "axios";
const http = axios.create()
http.get("http://api.luffycity.cn:8000/home/test").then(response=>{
    console.log(response.data);
})
</script>

<style scoped>

</style>
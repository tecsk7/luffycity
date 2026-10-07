import axios from "axios"

const http = axios.create({
  // timeout: 2500,                                 // 请求超时，有大文件上传需求关闭这个配置
  baseURL: "http://api.luffycity.cn:8000",          // 设置api服务端默认请求地址[如果基于服务端渲染的域名，这里可以填写api服务端的域名，如果基于Nodejs客户端服务器测试渲染服务端代码，这里不能带“/api服务端地址”]
  withCredentials: false,                           // 是否允许客户端ajax请求时携带cookie
})

// 请求拦截器
http.interceptors.request.use((config)=>{
  console.log("http请求之前");
  return config;
}, (error)=>{
  console.log("http请求错误");
  return Promise.reject(error);
});

// 响应拦截器
http.interceptors.response.use((response)=>{
  console.log("响应拦截器，在响应结果到达客户端的第一时间，执行then之前");
  return response;
}, (error)=>{
  console.log("服务器响应发生错误的时候，执行...");
  return Promise.reject(error);
});

export default http;
```[cite: 24]
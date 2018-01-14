1.获取所有国家

- 请求地址：http://127.0.0.1:5000/country/
- 请求方式：GET
- 返回数据格式：{"countrylist": [{"id": 10,"name": "china"},{"id": 11,"name": "japan"}]}

2.添加国家

- 请求地址：http://127.0.0.1:5000/country/
- 请求方式：POST
- 请求数据格式：{"name":"china"}
- 返回数据格式：
- {"code": 1, "id": 15,"message": "japan添加成功","name": "japan"}
- {"code": 0,"message": "该国家已存在！"}
 
3.根据id获取指定国家

- 请求地址：http://127.0.0.1:5000/country/\<int:id\>
- 请求方式：GET
- 返回数据格式：
- {"code": 1,"id": 13,"message": "成功获取china","name": "china"}
- {"code": 0,"message": "该国家不存在"}

4.根据id删除指定国家

- 请求地址：http://127.0.0.1:5000/country/\<int:id\>
- 请求方式：DELETE
- 返回数据格式：
- {"code": 0,"message": "该国家不存在"}
- {"code": 1,"message": "成功删除japan"}
 
5.获取所有城市

- 请求地址：http://127.0.0.1:5000/city/
- 请求方式：GET
- 返回数据格式：{ "citylist": [{"country": 10,"id": 4,"name": "hangzhou"},{"country": "中国“,"id": 5,"name": "beijing"}]}


6.添加城市

- 请求地址：http://127.0.0.1:5000/city/
- 请求方式：POST
- 数据请求格式：{"name":"shenzhen","countryname":"china"}
- 返回数据格式：
- {"code": 0,"message": "beijing已存在！"}
- {"code": 1,"country": "中国","id": 10,"message": "shanghai添加成功","name": "shanghai"}


7.通过id获取指定城市

- 请求地址：http://127.0.0.1:5000/city/\<int:id\>
- 请求方式：GET
- 响应数据：
- {"city": { "code": 1,"country": "中国","id": 5,"message": "成功查询到beijing","name": "beijing"}}
- {"city": {"code": 0,"message": "没有该城市！"}}

8.通过id删除指定城市

- 请求地址：http://127.0.0.1:5000/city/\<int:id\>
- 请求方式：DELETE
- 响应数据：
- {"code": 0,"message": "成功删除beijing"}
- {"code": 0,"message": "城市不存在"}

9.用户注册

- 请求地址：http://127.0.0.1:5000/register/
- 请求方式：POST
- 请求数据格式：form表单提交（username 、password 、email）
- 响应数据：
- { "code": 0,"message": "该用户名已被注册，请使用其他用户名！"}
- { "code": 1,"message": "注册成功！","username": "laowu3"}

10.用户登录

- 请求地址：http://127.0.0.1:5000/login/
- 请求方式：POST
- 请求数据格式：form表单提交（username 、password）
- 响应数据：
- { "code": 1,"message": "登录成功！"}
- { "code": 0, "message": "用户不存在"}
- { "code": 0,"message": "密码错误！"}

11.获取所有景点

- 请求地址：http://127.0.0.1:5000/spots/\<int:page>
- 请求方式：GET
- 响应数据：

```
{"重庆航空温泉 ": {
	
		"id": 218,

		"name": "重庆航空温泉 ",
		
		"city": "重庆",
    
		"provience": "重庆"，
    
		"adress": "重庆市重庆巴南区东泉镇。",
		    
		"price": "37",
		    
		"detail": "重庆航空温泉酒店是集餐饮、住宿、娱乐、休闲、泡浴、会议六大功能为一体的大型综合旅游度假酒店......",
		  
		"img\_url\_list": [
		"http://m.tuniucdn.com/filebroker/cdn/snc/c0/af/c0af4c31701924d24dc0d6ca5f11a8e7_w200_h200_c1_t0.jpg",
		"http://m.tuniucdn.com/filebroker/cdn/olb/fb/a9/fba9c75f897889a10b98d37cdfa4a563_w145_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/olb/cc/1d/cc1d5d5bd7999c1d70243890a5879e4b_w240_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/olb/0d/1a/0d1a04ed4528cc6a001a4d8cfe86f19d_w240_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/snc/c0/af/c0af4c31701924d24dc0d6ca5f11a8e7_w145_h95_c1_t0.jpg",
		""],}，
“崆山白云洞”:{...}
}
```

12.通过城市获取景点

- 请求地址：http://127.0.0.1:5000/spots/\<city>/\<page>
- 请求方式：GET
- 举例：http://127.0.0.1:5000/spots/Beijing/1
- <city>参数：城市参数，城市名的拼音全拼，首字母大写
- <page>参数：页数，每页10条记录
- 响应数据： 
  - 1.如果城市参数错误，返回以下数据：
    
    	{"code": 0,"message": "该城市名没有被记录！请查询其他城市！"}
  - 2.如果指定页面超过可查询页面范围，返回以下数据：
  
      {"code": 0,"message": "没有查询到数据！"}
  - 3.如果参数均正确，返回以下数据

```
{"重庆航空温泉 ": {
	
		"id": 218,

		"name": "重庆航空温泉 ",
		
		"city": "重庆",
    
		"provience": "重庆"，
    
		"adress": "重庆市重庆巴南区东泉镇。",
		    
		"price": "37",
		    
		"detail": "重庆航空温泉酒店是集餐饮、住宿、娱乐、休闲、泡浴、会议六大功能为一体的大型综合旅游度假酒店......",
		  
		"img\_url\_list": [
		"http://m.tuniucdn.com/filebroker/cdn/snc/c0/af/c0af4c31701924d24dc0d6ca5f11a8e7_w200_h200_c1_t0.jpg",
		"http://m.tuniucdn.com/filebroker/cdn/olb/fb/a9/fba9c75f897889a10b98d37cdfa4a563_w145_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/olb/cc/1d/cc1d5d5bd7999c1d70243890a5879e4b_w240_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/olb/0d/1a/0d1a04ed4528cc6a001a4d8cfe86f19d_w240_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/snc/c0/af/c0af4c31701924d24dc0d6ca5f11a8e7_w145_h95_c1_t0.jpg",
		""],}，
“崆山白云洞”:{...}
}
```


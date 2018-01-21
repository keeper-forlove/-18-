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

- 请求地址：http://127.0.0.1:5000/country/<int:id>
- 请求方式：GET
- 返回数据格式：
- {"code": 1,"id": 13,"message": "成功获取china","name": "china"}
- {"code": 0,"message": "该国家不存在"}

4.根据id删除指定国家

- 请求地址：http://127.0.0.1:5000/country/<int:id>
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

- 请求地址：http://127.0.0.1:5000/city/<int:id>
- 请求方式：GET
- 响应数据：
- {"city": { "code": 1,"country": "中国","id": 5,"message": "成功查询到beijing","name": "beijing"}}
- {"city": {"code": 0,"message": "没有该城市！"}}

8.通过id删除指定城市

- 请求地址：http://127.0.0.1:5000/city/<int:id>
- 请求方式：DELETE
- 响应数据：
- {"code": 0,"message": "成功删除beijing"}
- {"code": 0,"message": "城市不存在"}

9.用户注册

- 请求地址：http://127.0.0.1:5000/user/register/
- 请求方式：POST
- 请求数据格式：json
- 请求参数：username、password、mail:
- 响应数据：
	- 参数不全：{'code': 0, 'message': '请填写空缺数据'}
	- 用户名已存在：{'code': 1, 'message': '该用户已经存在,请更换用户名'}
	- 邮箱已存在：{'code': 2, 'message': '此邮箱已注册,请更换邮箱'}
	- 成功：{'code': 3, 'message': '请前往邮箱激活账号'}

10.用户登录

- 请求地址：http://127.0.0.1:5000/user/login/
- 请求方式：POST
- 请求数据格式：json
- 请求参数：username_or_mail、password
- 响应数据：
	- 登录成功：{'code': 1, 'message': '登陆成功','id':u_username.id}
	- 登录失败：
		- 情况1：{'code': 0, 'message': '登录失败,用户邮箱未激活'}
		- 情况2：{'code': 0, 'message': '用户名与密码不匹配'}
		- 情况3：{'code': 0, 'message': '邮箱与密码不匹配'}
		- 情况4：{'code': 0, 'message': '登录失败,用户邮箱未激活'}
		- 情况5：{'code': 0, 'message': '用户名或邮箱不存在'}
		- 情况6：{'code':0,'message':'数据格式错误'}
		
		


11.获取景点数据

- 请求地址：http://127.0.0.1:5000/spots
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
  - sort参数（可选）：排序方式，可选（parice,rank,score,name)
- 例子：http://127.0.0.1:5000/spots?limit=5&page=1
- 响应结果：
  - 1.数据超出查询范围：
```
 {"code": 0,"message": "请求页面超出数据量查询范围！"}
```
	
  - 2.正常返回结果：

```
#common说明：common整体是评论列表，其中每条是一个元组,格式如：[(uid,create_time,content),(),()...]
{
    "code": 1,
    "message": "查询成功",
    "data_list": [
    {
	
		"id": 218,

		"name": "重庆航空温泉 ",
		
		"city": "重庆",
		"common": [
                [4,"Fri, 19 Jan 2018 03:42:38 GMT","常州真好玩"]，
    
                ]
 
		"provience": "重庆"，
    
		"adress": "重庆市重庆巴南区东泉镇。",
		    
		"price": "37",
		"score":10,
		"rank":5,
		    
		"detail": "重庆航空温泉酒店是集餐饮、住宿、娱乐、休闲、泡浴、会议六大功能为一体的大型综合旅游度假酒店......",
		  
		"img\_url\_list": [
		"http://m.tuniucdn.com/filebroker/cdn/snc/c0/af/c0af4c31701924d24dc0d6ca5f11a8e7_w200_h200_c1_t0.jpg",
		"http://m.tuniucdn.com/filebroker/cdn/olb/fb/a9/fba9c75f897889a10b98d37cdfa4a563_w145_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/olb/cc/1d/cc1d5d5bd7999c1d70243890a5879e4b_w240_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/olb/0d/1a/0d1a04ed4528cc6a001a4d8cfe86f19d_w240_h95_c1_t0.png",
		"http://m.tuniucdn.com/filebroker/cdn/snc/c0/af/c0af4c31701924d24dc0d6ca5f11a8e7_w145_h95_c1_t0.jpg",
		""],}，
{		
	"id": 218,

	"name": "重庆航空温泉 ",
	...
}
]
```

12.根据城市获取景点数据

- 请求地址：http://127.0.0.1:5000/spots/<string:city>
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
  - sort参数（可选）：排序方式，可选（parice,rank,score,name)
- 例子：http://127.0.0.1:5000/spots/Beijing?limit=5&page=10
- 响应结果：
  - 1.数据超出查询范围：
```
 {"code": 0,"message": "请求页面超出数据量查询范围！"}
```
	
  - 2.正常返回结果：

```
{
    "code": 1,
    "message": "查询成功",
    "data_list": [
    {
	
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
{		
	"id": 218,

	"name": "重庆航空温泉 ",
	...
}
]
```


13.获取酒店数据

- 请求地址：http://127.0.0.1:5000/hotels
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
  - sort参数（可选）：排序方式，可选（parice,rank,score,name)
- 例子：http://127.0.0.1:5000/hotels?limit=5&page=1
- 响应结果：同上(api12)
 ```

14.根据城市获取酒店数据

- 请求地址：http://127.0.0.1:5000/hotels/<string:city>
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
  - sort参数（可选）：排序方式，可选（parice,rank,score,name)
- 例子：http://127.0.0.1:5000/hotels/Beijing?limit=5&page=10
- 响应结果：同上(api12)
 ```

15.获取美食数据

- 请求地址：http://127.0.0.1:5000/foods
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
  - sort参数（可选）：排序方式，可选（parice,score,name)
- 例子：http://127.0.0.1:5000/foods?limit=5&page=1
- 响应结果：同上(api12)
 ```

16.根据城市获取美食数据

- 请求地址：http://127.0.0.1:5000/foods/<string:city>
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
  - sort参数（可选）：排序方式，可选（parice,score,name)
- 例子：http://127.0.0.1:5000/foods/Beijing?limit=5&page=10
- 响应结果：同上(api12)
 ```
 
17.发布评论

- 请求地址：http://127.0.0.1:5000/article/comments
- 请求方式：POST
- 请求参数：
 
 ```python
 type:类型，可选值（'spots'、'hotels'、‘foods'、'shops')
 
 tid:该条数据对应的id
 
 uid:发布评论者的id
 
 content:评论内容
 ```
- 响应结果：{ "code": 1, "message": "添加成功！" }


18.发布游记

- 请求地址：http://127.0.0.1:5000/article/experience
- 请求方式：POST
- 请求参数：

```python
"uid":发布者id
"type":游记类型（'spots'、'hotels'、‘foods'、'shops')
"title"：游记标题
"content":游记内容
"city"：属于哪个城市的游记
```

- 响应结果：同上(api17)

19.获取所有游记

- 请求地址：http://127.0.0.1:5000/experiences
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
- 举例：http://127.0.0.1:5000/experiences?limit=5&page=1
- 响应结果：

```
{
   
    "code": "1",
   
    "data_list": [
        
        {
            "city": "北京",
            "content": "这个景点真好，非常喜欢",
            "create_time": "Tue, 16 Jan 2018 13:45:04 GMT",
            "id": 1,
            "title": "北京游览心得",
            "type": "景点",
            "uid": 4
        }
    ],
    
    "message": "成功！",
    
    "type": "experience"
}
```

20.根据城市获取所有游记

- 请求地址：http://127.0.0.1:5000/experiences/<string:city>
- 请求方式：GET
- get传参数：
  - page参数：请求第几页数据
  - limit参数：每页请求多少条数据
- 举例：http://127.0.0.1:5000/experiences/Beijing/?limit=5&page=1
- 响应结果：同上（api19)
<template>
<!--这是“我的”页面-->
    <div class="app-main">
        <div class="header">
            <mt-button class="btn-header" type="default" size="small">消息</mt-button>
            <mt-button class="btn-header" type="default" size="small">设置</mt-button>
        </div>
        <div class="personal">
            这是个人信息区域，站定
        </div> 
        <div class="content">
            <div class="mine-section" v-for="mine in mines" :key="mine">
                    <i class="yo-ico">&#xf04b;</i>
                    <span> {{mine}}</span>
            </div>
        </div>

    </div>
    
</template>
<script>
export default {
  data(){
      return {
          mines:["我的订单","我的游记","我的收藏","我的钱包","我的问答","我的点评","优惠券","我的下载","我的活动"]
      }
  }
}
</script>
<style lang="scss" scoped>
    .header{
        height:50px;background:#ccc;display:flex;flex-direction: row-reverse;align-items: center;padding-right:20px;
        .btn-header{
            margin-left:10px;height:26px;
        }
    }
    .personal{height:2rem;background:rgb(116, 116, 145);}
    .content{
        display:flex;flex-wrap:wrap;
            .mine-section{
            width:33.3%;height:1.2rem;display:flex;flex-direction: column;align-items:center;justify-content:center;
         }
    }
   
</style>

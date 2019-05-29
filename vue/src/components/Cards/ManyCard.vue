<template>
  <div class="section ">
    <div class="container">
      <div class="title">
        <h3>授業一覧</h3>
      </div>
      <div class="row">
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- card1 -->
          <Card2/>
        </div>
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- Tabs with Background on Card2 -->
          <Card2/>
          <!-- End Tabs on plain Card -->
        </div>
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- Tabs with Background on Card2 -->
          <Card2/>
          <!-- End Tabs on plain Card -->
        </div>
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- Tabs with Background on Card2 -->
          <Card2/>
          <!-- End Tabs on plain Card -->
        </div>
                <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- card1 -->
          <Card2/>
        </div>
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- Tabs with Background on Card2 -->
          <Card2/>
          <!-- End Tabs on plain Card -->
        </div>
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- Tabs with Background on Card2 -->
          <Card2/>
          <!-- End Tabs on plain Card -->
        </div>
        <div class="col-md-6 ml-auto col-lg-3 mr-auto">
          <!-- Tabs with Background on Card2 -->
          <Card2/>
          <!-- End Tabs on plain Card -->
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Card, Tabs, TabPane } from '@/components';
import Card2 from '@/components/Cards/Card2'

export default {
  components: {
    Card,
    Tabs,
    TabPane,
    Card2
  }
};
</script>
<style>
.tab-content.tab-content-padding {
  padding: 40px;
}

.col-md-6 {
    padding : 20px ;
}
</style>
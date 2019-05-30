<template>
  <div class="section ">
    <div class="container">
      <div class="title">
        <h3>授業一覧</h3>
      </div>
      <div class="row">
        <div class="col-md-6 ml-auto col-lg-3 mr-auto" v-for="le in lectures"  :key="le.id">
          <!-- card1 -->
          <div>
            <b-card
              title= "title"
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                <p>{{le.content}}</p>
              </b-card-text>

              <b-button id="show-btn" @click="openModal(le)" href="#" variant="primary">Go somewhere</b-button>
             </b-card>
          </div>
        </div>
      </div>
    </div>
  <div>
    <modal :val="item" v-if="showModal" @close="closeModal"></modal>
  </div>
  
  </div>
</template>
<script>
import { Card, Tabs, TabPane } from '@/components';
import Card2 from '@/components/Cards/Card2'
import modal from '@/components/Cards/modal.vue'
import Vue from 'vue'

export default {
  components: {
    modal,
    Card,
    Tabs,
    TabPane,
    Card2
  },
  props: {
    lectures: Array,
  },
  data() {
    return {
      showModal: false,
      item:'',
    }
  },
methods: {
  openModal(le) {
    this.item = le;
    this.showModal = true;
  },
  closeModal() {
    this.showModal = false;
  }
},
}
</script>
<style>
.tab-content.tab-content-padding {
  padding: 40px;
}

.col-md-6 {
    padding : 20px ;
}

</style>
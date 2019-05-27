<template>
  <div>
    <form @submit.prevent="onSubmit">
      <div class="form-item">
          <vue-input name="input" v-model="form.input"></vue-input>
      </div>
       <div class="form-item">
        <button type="submit">送信</button>
      </div>
    </form>

    <time-line :timelines="timelines" label="TimeLine" name="timeline"></time-line>
  </div>
</template>

<script>
import Vue from 'vue'
import Input from './Input'
import TimeLine from './TimeLine'
import data from '../assets/data.json'

export default {
  components: {
    TimeLine,
    Input
  },
  data () {
    return {
      timelines: data.timelines,
      form: {
        input: 'Search'
      }
    }
  },
  methods: {
    onSubmit () {
        console.log('送信')
      }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
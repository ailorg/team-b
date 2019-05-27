<template>
    <time-line :timelines="timelines"></time-line>
</template>

<script>
import Vue from 'vue';
import TimeLine from './TimeLine'
import data from '../assets/data.json'

export default {
  components: {
    TimeLine
  },
  data () {
    return {
      timelines: data.timelines
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
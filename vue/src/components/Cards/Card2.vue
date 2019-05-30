<template>
<div>
  <!--使ってない-->
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
      <p>{{lecture.content}}</p>
    </b-card-text>

    <b-button href="#" variant="primary">Go somewhere</b-button>
  </b-card>
</div>
</template>

<script>
  export default {
    name: 'card2',
    props: {
      lecture: Object,
    },
    data () {
       return {
         imgSrc: "..."
       }
    }
  }
</script>

<style>
</style>
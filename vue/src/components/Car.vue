<template>
  <p>{{lecture.date}} - {{lecture.name}}</p>
</template>

<script>
export default {
  props: {
    lecture: Object,
  }
}
</script>
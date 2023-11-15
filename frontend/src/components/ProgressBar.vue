<script setup lang="ts">
  import {computed} from 'vue'

  interface IProgressBarProps {
    data: any,
  }

  const props = withDefaults(defineProps<IProgressBarProps>(), {
    data: {},
  });
  const width = computed(() => {
    if (props.data) {
      if (props.data.total === props.data.done) {
      return 100
    }
    return Math.floor(100/props.data.total) * props.data.done 
    }

  })

</script>

<template>
<div class="progressBar">
  <span class='progress' :style="{width: `${width}%`}"></span>
</div>
</template>

<style scoped>

.progressBar {
  position: relative;
  max-width: 500px;
  width: 100%;
  margin: 30px auto 0;
  height: 30px;
  background: #274545;
  overflow: hidden;
  border-radius: 3.125rem;
}

span.progress {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 0%;
  background: #326666;
  transition: all .3s;
}

</style>

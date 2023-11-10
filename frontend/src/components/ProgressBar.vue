<script setup lang="ts">
  import {computed} from 'vue'
  interface IProgressBarProps {
    data: {},
  }

  const props = withDefaults(defineProps<IProgressBarProps>(), {
    data: {},
  });
  const width = computed(() => {
    if (props.data.total === props.data.done) {
      return 100
    }
    return Math.floor(100/props.data.total) * props.data.done 
  })
  const progressStyle = computed(() => {
    return {
  position: 'absolute',
  left: 0,
  top: 0,
  bottom: 0,
  width: `${width.value}%`,
  background: '#326666',
  transition: 'all .3s',
}
  })
</script>

<template>
  <div class="counter">{{ props.data }}</div>
<div class="progressBar">
  <span :style="progressStyle"></span>
</div>
</template>

<style>
.progressBar {
  position: relative;
  max-width: 500px;
  width: 100%;
  margin: 30px auto 0;
  height: 30px;
  background: #274545;
  overflow: hidden;
}

span.progress {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 50%;
  background: #326666;
  transition: all .3s;
}


</style>

<script setup lang="ts">
  interface IProgressBarProps {
    status: string,
  }

  const props = withDefaults(defineProps<IProgressBarProps>(), {
    status: '',
  });
</script>

<template>
  <div class="counter">{{ props.status }}</div>
<div class="progressbar">
  <span class="progress"></span>
</div>
</template>

<style>
.progressbar {
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
  width: 0;
  background: #326666;
  transition: all .3s;
}


</style>

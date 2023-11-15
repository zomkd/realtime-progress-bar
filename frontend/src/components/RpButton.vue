<script setup lang="ts">
  import type { ButtonHTMLAttributes } from 'vue';

  interface IButtonProps {
    text: string,
    type: ButtonHTMLAttributes['type'],
    class: string,
  }

  const props = withDefaults(defineProps<IButtonProps>(), {
    text: '',
    type: 'submit',
    class: 'default-btn'
  });

  const emit = defineEmits(['clicked']);

  const handleClick = () => {
    emit('clicked')
  }
</script>

<template>
  <button
    :type="props.type"
    :class="props.class"
    @click="handleClick"
  >
    {{ props.text }}
  </button>
</template>

<style scoped>
.default-btn {
    background-color: aquamarine;
    height: 3rem;
    width: 5rem;
    color: black
}

.stop-btn {
  background-color: rgb(241, 122, 122);
  height: 3rem;
  width: 5rem;
  color: black
}
</style>

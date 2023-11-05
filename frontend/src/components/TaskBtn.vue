<script setup lang="ts">
  import type { ButtonHTMLAttributes } from 'vue';

  interface IButtonProps {
    text: string,
    type: ButtonHTMLAttributes['type'],
  }

  const props = withDefaults(defineProps<IButtonProps>(), {
    text: '',
    type: 'submit',
  });

  const emit = defineEmits(['clicked']);
</script>

<template>
  <button
    :type="props.type"
    class="btn"
    @click="emit('clicked')"
  >
    {{ props.text }}
  </button>
</template>

<style>
.btn {
    background-color: aquamarine;
    height: 3rem;
    width: 5rem;
    color: black
}
</style>

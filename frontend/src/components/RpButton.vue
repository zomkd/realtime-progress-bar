<script setup lang="ts">
  import type { ButtonHTMLAttributes } from 'vue';

  interface IButtonProps {
    text: string,
    type: ButtonHTMLAttributes['type'],
    disabled: boolean,
  }

  const props = withDefaults(defineProps<IButtonProps>(), {
    text: '',
    type: 'submit',
    disabled: false,
  });

  const emit = defineEmits(['clicked']);

  const handleClick = () => {
    emit('clicked')
  }
</script>

<template>
  <button
    :disabled="props.disabled"
    :type="props.type"
    class="default-btn"
    :class="{'disabled' : disabled}"
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
.disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>

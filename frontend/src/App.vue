<script setup lang="ts">
import { onMounted,ref } from 'vue'
import ProgressBar from './components/ProgressBar.vue';
import TaskBtn from './components/TaskBtn.vue';
const data = ref()
const inputData = ref()

const BASE_URL = 'http://127.0.0.1:8000';
const BASE_URL_WS = 'ws://127.0.0.1:8000';

function submit()  {
  fetch(BASE_URL + '/task', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
          task_name: "task_1",
    }),
  })
  .then(res => res.json())
  .then((res) => {
    const socket = new WebSocket(
      BASE_URL_WS + `/task/${res.task_id}`
        );
        socket.onmessage = (event) => {
          const parsedEvent = JSON.parse(event.data);
          console.log(parsedEvent);
          // data.value = parsedEvent.progress * 100;
          data.value = parsedEvent
        };

        socket.onerror = (err) => {
          console.log(err);
        };
        socket.onclose = (event) => {
          console.log(event);
        };
        socket.onopen = (event) => {
          console.log(event);
        };
  }).catch(err => console.log(err))
}
</script>

<template>
  <div class="container">
    <div class="task-box">
      <progress-bar :data="data?.task_result" />
      <task-btn type="submit" @clicked="submit" text="click!"/>
    </div>
</div>
</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
} 
.task-box {
  width: 31.25rem
}
</style>

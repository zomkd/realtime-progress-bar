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
  <progress-bar :status="data"/>

  <task-btn @clicked="submit" text="click!"/>
  <!-- <h1>hello {{data}}</h1> -->
  <input type="text" v-model="inputData" @keyup.enter="submit()">
  <!-- <button @click="submit()">submit</button> -->
  <RouterView />
</template>

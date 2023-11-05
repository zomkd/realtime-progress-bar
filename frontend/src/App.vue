<script setup lang="ts">
import { onMounted,ref } from 'vue'
import ProgressBar from './components/ProgressBar.vue';
import TaskBtn from './components/TaskBtn.vue';
const data = ref()
const inputData = ref()
const connection = new WebSocket("ws://localhost:8000/ws")

const BASE_URL = 'http://localhost:8000/';
const BASE_URL_WS = 'ws://localhost:8000/';

function submit()  {
  fetch(BASE_URL + '/task', {
    method: "POST",
    headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
    },
    body: JSON.stringify({
          task_name: "task_1",
    }),
  }).then(res => res.json()).then((res) => {
    const socket = new WebSocket(
      BASE_URL_WS + `task/${res.celery_task_id}/`
        );
        socket.onmessage = (event) => {
          const parsedEvent = JSON.parse(event.data);
          console.log(parsedEvent);
          data.value = parsedEvent.progress * 100;
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
  })
  connection.send(inputData.value)
}


onMounted(() => {

  connection.onmessage = function(e){

    data.value = e.data

  }

})

</script>

<template>
  <progress-bar :status="data"/>

  <task-btn @clicked="submit" @keyup.enter="submit()" text="click!"/>
  <!-- <h1>hello {{data}}</h1> -->
  <input type="text" v-model="inputData" @keyup.enter="submit()">
  <!-- <button @click="submit()">submit</button> -->
  <RouterView />
</template>

<template>
    <div>
        <pretty-chat-window 
            projectID="794653df-052a-4ad2-b0aa-d6c251a10aef"
            v-bind:userName="username"
            v-bind:userSecret="secret" 
        />
    </div>  
</template>

<script>
import { PrettyChatWindow } from 'react-chat-engine-pretty';

export default {
    components: { 'pretty-chat-window': PrettyChatWindow },
    props: {
        username: {
            type: String,
            required: true,
        },
        secret: {
            type: String,
            required: true,
        },
    },
}
</script>  

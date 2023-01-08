<template>
    <PrettyChatWindow
        projectId="794653df-052a-4ad2-b0aa-d6c251a10aef"
        :username="username"
        :secret="secret" 
    />
</template>

<script>
import { PrettyChatWindow } from 'react-chat-engine-pretty';
import { applyReactInVue } from 'veaury'

export default {
    components: { 
        PrettyChatWindow: applyReactInVue(PrettyChatWindow)
    },
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

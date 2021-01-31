<template>
    <div class='column is-9'>
        <div class="control textarea-container has-fixed-size">
            <textarea class="textarea" placeholder="Text input" rows="1" v-model="input_txt"></textarea>
            <div class="dropdown is-up is-hoverable">
                <div class="dropdown-trigger mt-2 mr-5">
                    <span>
                        <i class="fas fa-2x fa-paper-plane"></i>
                    </span>
                </div>
                <div class="dropdown-menu" id="dropdown-menu7" role="menu">
                    <div class="dropdown-content popup-item-border">
                        <div class="dropdown-item popup-item-width">
                            <button class="btn_reactions" @click="submit('Sad.svg')">
                                <img src="../assets/mini-emoji/Sad.svg">
                            </button>
                            <button class="btn_reactions" @click="submit('Happy.svg')">
                                <img src="../assets/mini-emoji/Happy.svg">
                            </button>
                            <button class="btn_reactions" @click="submit('Surprised.svg')">
                                <img src="../assets/mini-emoji/Surprised.svg">
                            </button>
                            <button class="btn_reactions" @click="submit('Anger.svg')">
                                <img src="../assets/mini-emoji/Anger.svg">
                            </button>
                            <button class="btn_reactions" @click="submit('Fear.svg')">
                                <img src="../assets/mini-emoji/Fear.svg">
                            </button>
                            <button class="btn_reactions" @click="submit('Disgust.svg')">
                                <img src="../assets/mini-emoji/Disgust.svg">
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {

    name: 'ChatInput',
    props: {
        msg: String,
    },
    methods: {
        send_message(msg) {
            const url = "http://localhost:5000/text-input";
            axios.post(url, msg)
                .catch((error) => { console.log(error); });
        },

        submit(emoji) {
            if (this.input_txt.trim().length > 0) {
                this.msg_id++;
                var today = new Date();
                var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
                const msg = {
                    txt: this.input_txt,
                    id: this.msg_id,
                    time: time,
                    emoji: emoji,
                };
                this.update_history(msg);
                this.send_message(msg);
                this.input_txt = "";
            } else(
                console.log("Input is empty!")
            )
        },
        update_history(msg) {
            //EventBus.$emit('msg_history_update', msg);
            this.$eventHub.$emit('msg_history_update', msg);
        },
    },
    data: function() {
        return {
            input_txt: null,
            msg_id: 0,

        }
    },
}
</script>
<style scoped>
textarea {
    border-width: 0;
    resize: none;
    background: #fafafa;
    border-radius: 30px;
}

.textarea-container {
    position: relative;
}

.textarea-container textarea {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
}

.textarea-container .dropdown {
    position: absolute;
    top: 0;
    right: 0;
}

.popup-item-width {
    width: 10rem;
}

.popup-item-border {
    border-radius: 30px;
    width: 10rem;
}

.btn_reactions {
    border-radius: 30px;
    outline: 0;
}

.btn_reactions:hover {
    box-shadow: 0 0 4pt 1pt rgba(30, 136, 229, 0.5);
    background: rgba(30, 136, 229, 0.5);
}

.btn_reactions:active {
    box-shadow: 0 0 4pt 1pt rgba(30, 136, 229, 0.5);
    background: rgba(30, 136, 229, 0.8);
}

button {
    background: Transparent;
    border: 0px;
    outline: 0;
}

img {
    width: 30px;
    height: 30px;
}

.dropdown-menu {
    right: 0;
    left: auto;
}
</style>

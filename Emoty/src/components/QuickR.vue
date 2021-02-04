<template>
    <div class='column is-3'>
        <div class="dropdown is-up is-hoverable fit-button">
            <div class="dropdown-trigger fit-button">
                <button class="button quick-r" aria-haspopup="true" aria-controls="dropdown-menu7">
                    <span class="has-text-centered has-text-weight-semibold is-size-5 has-text-black">Quick Reaction</span>
                    <span class="icon is-small">
                        <i class="fas fa-comments" aria-hidden="true"></i>
                    </span>
                </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu7" role="menu">
                <div class="dropdown-content popup-item-border">
                    <QReactionView v-on:selectedReaction="submittedQuickReaction" v-for="r in list" :reaction="r" :key="r.id" />
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import QReactionView from './QReactionView.vue'

export default {
    name: 'QuickR',
    components: {
        QReactionView
    },
    props: {
        msg: String
    },
    methods: {
        submittedQuickReaction(reaction) {
            this.send_quick_reaction(reaction.id, reaction.key);
            this.update_history(reaction.key, reaction.emoji);
        },
        send_quick_reaction(reaction_id, reaction_key) {
            const url = "http://localhost:5000/submitted_qr";
            var msg = {
                id: reaction_id,
                key: reaction_key
            };
            axios.post(url, msg)
                .catch((error) => { console.log(error); });

        },
        update_history(key, emoji) {
            var today = new Date();
            var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
            var idRandom = Math.random();
            const msg = {
                txt: key,
                id: idRandom,
                time: time,
                emoji: emoji,
            };
            this.$eventHub.$emit('msg_history_update', msg);
        },
        receive_re_list() {
            const url = "http://localhost:5000/quick-re";
            axios.get(url)
                .then(response => {
                    this.list = response.data.re_list
                })
                .catch((error) => { console.log(error); });

        },
    },

    created() {
        this.receive_re_list();
        console.log(this.list);
    },
    data() {
        return {
            list: [],
            reaction: {},
        }
    }

}
</script>
<style scoped>
.quick-r {
    height: 100%;
    width: 100%;
    border-radius: 35px;
    border: 0px;
}

.fit-button {
    height: 100%;
    width: 100%;
    padding: 0px 0px !important;
}

.popup-item-border {
    border-radius: 30px;
}
</style>

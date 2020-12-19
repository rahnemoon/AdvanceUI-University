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
      <div class="dropdown-item popup-item-width">
        <p>&#129409; {{list}}</p>
      </div><hr>
    </div>
  </div>
</div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'QuickR',
  props: {
    msg: String
  },
  methods: {
    receive_re_list(){
      const url = "http://localhost:5000/quick-re";
      axios.get(url)
      .then(response=>{
        this.list = response.data
      })
      .catch((error) => {console.log(error);});
      
    },
    },
    
    created() {
    this.receive_re_list();
    console.log(this.list);
        },
    data(){
    return {
      list: [],
    }
  }
    
    
}
</script>


<style scoped>
.popup-item-width{
  min-width: 21rem;
}
.popup-item-border{
  border-radius: 30px;
}
hr{
  margin: 0 0 0 0px;
}

.quick-r{
  height: 100%;
  width: 100%;
  border-radius: 35px;
  border: 0px;
}

.fit-button{
  height: 100%;
  width: 100%;
  padding: 0px 0px !important;
}
</style>

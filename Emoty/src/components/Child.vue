<template>
  <div style="padding-top: calc((100vh - 70vh)/2)">
    <audio id="audiofile" :src="linkAudio" controls></audio><br>
    <div id="subtitles"></div>

    <h2>{{mouthCues}} {{metadata}}</h2>
    <h1 class="circle">
    <div id="titleBox">
</div>
        <button @click="emotion_recreation" id="masterControl">hello</button>

    <div id="controls" ref="controls">
    <button id="masterControl">action</button>
    </div>

    <svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path id="hair" d="M254.07 167.395L252.573 167.498L254.07 167.395ZM261.009 156.956C261.595 157.542 262.544 157.542 263.13 156.956C263.716 156.37 263.716 155.42 263.13 154.834L261.009 156.956ZM250.668 158.729C251.497 158.729 252.168 158.058 252.168 157.229C252.168 156.401 251.497 155.729 250.668 155.729L250.668 158.729ZM256 175.5C254.573 175.038 254.573 175.038 254.573 175.037C254.573 175.037 254.574 175.036 254.574 175.035C254.574 175.034 254.574 175.033 254.575 175.032C254.575 175.031 254.576 175.029 254.576 175.027C254.577 175.024 254.578 175.022 254.579 175.02C254.58 175.016 254.581 175.014 254.581 175.013C254.581 175.013 254.581 175.015 254.58 175.017C254.569 175.041 254.584 174.996 254.645 174.921C254.664 174.898 254.972 174.501 255.584 174.494C256.266 174.487 256.577 174.957 256.584 174.968C256.613 175.01 256.562 174.945 256.472 174.638C256.389 174.352 256.292 173.925 256.188 173.307C255.981 172.072 255.765 170.17 255.566 167.292L252.573 167.498C252.775 170.42 252.999 172.431 253.229 173.803C253.344 174.489 253.464 175.039 253.592 175.477C253.713 175.893 253.866 176.297 254.085 176.627C254.284 176.926 254.773 177.503 255.617 177.494C256.389 177.486 256.839 176.978 256.977 176.808C257.156 176.587 257.266 176.36 257.32 176.238C257.351 176.167 257.376 176.106 257.393 176.06C257.402 176.036 257.409 176.016 257.414 176C257.417 175.991 257.42 175.984 257.422 175.978C257.423 175.975 257.424 175.972 257.425 175.969C257.425 175.968 257.426 175.966 257.426 175.965C257.426 175.964 257.426 175.964 257.427 175.963C257.427 175.962 257.427 175.962 256 175.5ZM255.566 167.292C255.182 161.72 256.532 158.741 257.878 157.433C259.214 156.134 260.465 156.412 261.009 156.956L263.13 154.834C261.174 152.878 258.025 153.106 255.787 155.282C253.557 157.449 252.157 161.47 252.573 167.498L255.566 167.292ZM254.128 169.887C249.917 166.219 248.765 163.157 248.792 161.281C248.818 159.418 249.899 158.729 250.668 158.729L250.668 155.729C247.902 155.729 245.836 158.117 245.792 161.239C245.748 164.348 247.601 168.18 252.158 172.149L254.128 169.887Z" fill="black"/>
    <g id="body" ref="body">
    <path d="M329 246C329 204.579 295.421 171 254 171C212.579 171 179 204.579 179 246V321C179 334.807 190.193 346 204 346C213.765 346 222.161 339.214 230.348 332.598C233.737 329.859 237.091 327.149 240.49 324.961C244.386 322.454 249.023 321 254 321C258.977 321 263.614 322.454 267.51 324.961C270.909 327.149 274.263 329.859 277.652 332.598C285.839 339.214 294.235 346 304 346C317.807 346 329 334.807 329 321V246Z" fill="#FBB03B"/>
    <path d="M303 249.66C300.238 244.877 301.877 238.761 306.66 236L315.32 231C320.103 228.239 326.219 229.877 328.981 234.66L356.481 282.292C360.623 289.466 358.165 298.64 350.99 302.782C343.816 306.924 334.642 304.466 330.5 297.292L303 249.66Z" fill="#FBB03B"/>
    <path d="M179 234.66C181.761 229.877 187.877 228.239 192.66 231L201.32 236C206.103 238.761 207.742 244.877 204.981 249.66L177.481 297.292C173.339 304.466 164.165 306.924 156.99 302.782C149.816 298.64 147.358 289.466 151.5 282.292L179 234.66Z" fill="#FBB03B"/>
    </g>
    <g id="natural_eye">
    <path id="nelo" d="M246 223C246 232.941 237.941 241 228 241C218.059 241 210 232.941 210 223C210 213.059 218.059 205 228 205C237.941 205 246 213.059 246 223Z" fill="white"/>
    <path id="neli" d="M238 223C238 228.523 233.523 233 228 233C222.477 233 218 228.523 218 223C218 217.477 222.477 213 228 213C233.523 213 238 217.477 238 223Z" fill="black"/>
    <path id="nero" d="M298 223C298 232.941 289.941 241 280 241C270.059 241 262 232.941 262 223C262 213.059 270.059 205 280 205C289.941 205 298 213.059 298 223Z" fill="white"/>
    <path id="neri" d="M290 223C290 228.523 285.523 233 280 233C274.477 233 270 228.523 270 223C270 217.477 274.477 213 280 213C285.523 213 290 217.477 290 223Z" fill="black"/>
    </g>

    <g id="angry_eye">

    <path id="aelo" d="M210 223C210 215.925 214.082 209.803 220.019 206.861L245.63 219.351C245.873 220.529 246 221.75 246 223C246 226.428 245.042 229.633 243.378 232.36C240.218 230.345 234.513 229 228 229C221.487 229 215.782 230.345 212.622 232.36C210.958 229.633 210 226.428 210 223Z" fill="white"/>
    <path id="aeli" d="M235.485 229.632C237.05 227.867 238 225.544 238 223C238 217.477 233.523 213 228 213C222.477 213 218 217.477 218 223C218 225.544 218.95 227.867 220.515 229.632C222.795 229.226 225.329 229 228 229C230.671 229 233.205 229.226 235.485 229.632Z" fill="black"/>

    <path id="aero" d="M262 223C262 221.75 262.127 220.529 262.37 219.351L287.981 206.861C293.918 209.803 298 215.925 298 223C298 226.428 297.042 229.633 295.378 232.36C292.218 230.345 286.513 229 280 229C273.487 229 267.782 230.345 264.622 232.36C262.958 229.633 262 226.428 262 223Z" fill="white"/>
    <path id="aeri" d="M287.485 229.632C289.05 227.867 290 225.544 290 223C290 217.477 285.523 213 280 213C274.477 213 270 217.477 270 223C270 225.544 270.95 227.867 272.515 229.632C274.795 229.226 277.329 229 280 229C282.671 229 285.205 229.226 287.485 229.632Z" fill="black"/>

    </g>
    <g id="supperise">
    <path id="selo" d="M246 223C246 232.941 237.941 241 228 241C218.059 241 210 232.941 210 223C210 213.059 218.059 205 228 205C237.941 205 246 213.059 246 223Z" fill="white"/>
    <path id="seli" d="M240 223C240 229.627 234.627 235 228 235C221.373 235 216 229.627 216 223C216 216.373 221.373 211 228 211C234.627 211 240 216.373 240 223Z" fill="black"/>
    <path id="sero" d="M298 223C298 232.941 289.941 241 280 241C270.059 241 262 232.941 262 223C262 213.059 270.059 205 280 205C289.941 205 298 213.059 298 223Z" fill="white"/>
    <path id="seri" d="M292 223C292 229.627 286.627 235 280 235C273.373 235 268 229.627 268 223C268 216.373 273.373 211 280 211C286.627 211 292 216.373 292 223Z" fill="black"/>
    </g>

    <g id="sad">
    <path id="saelo" d="M238.768 208.575C236.648 211.64 231.032 214.88 224.01 216.761C218.982 218.109 214.229 218.493 210.699 218.016C210.244 219.599 210 221.271 210 223C210 226.735 211.138 230.204 213.085 233.08C216.321 231.221 221.794 230 228 230C234.206 230 239.679 231.222 242.915 233.08C244.862 230.204 246 226.735 246 223C246 217.097 243.158 211.857 238.768 208.575Z" fill="white"/>
    <path id="saeli" d="M217.067 218.047C216.382 219.557 216 221.234 216 223C216 226.043 217.133 228.821 218.999 230.937C221.647 230.341 224.721 230 228 230C231.279 230 234.353 230.341 237.001 230.937C238.867 228.821 240 226.043 240 223C240 218.578 237.609 214.715 234.048 212.634C231.374 214.253 227.909 215.717 224.01 216.761C221.597 217.408 219.248 217.833 217.067 218.047Z" fill="black"/>
    <path id="saero" d="M294.915 233.08C291.679 231.221 286.206 230 280 230C273.794 230 268.321 231.221 265.085 233.08C263.138 230.204 262 226.735 262 223C262 217.272 264.676 212.169 268.845 208.872C271.113 211.848 276.592 214.941 283.387 216.761C288.695 218.184 293.696 218.532 297.276 217.928C297.747 219.537 298 221.239 298 223C298 226.735 296.862 230.204 294.915 233.08Z" fill="white"/>
    <path id="saeri" d="M289.001 230.937C286.353 230.341 283.279 230 280 230C276.721 230 273.647 230.341 270.999 230.937C269.133 228.821 268 226.043 268 223C268 218.704 270.258 214.935 273.652 212.815C276.282 214.362 279.634 215.756 283.387 216.761C286.033 217.471 288.603 217.913 290.959 218.103C291.628 219.598 292 221.256 292 223C292 226.043 290.867 228.821 289.001 230.937Z" fill="black"/>


    </g>
    <path id="nm" d="M256.072 265C251.972 265 248.159 264.747 244.875 264.407C238.849 263.808 232.873 262.717 227 261.144L227.54 259C227.834 259.083 256.928 267.421 280.346 259L281 261.112C272.757 264.082 263.889 265 256.072 265Z" fill="black"/>

    <path id="am" d="M251.108 259C266.955 259 280.794 268.103 281 268.242L279.814 270C279.514 269.799 249.658 250.192 228.453 269.898L227 268.349C234.543 261.335 243.083 259 251.108 259Z" fill="black"/>

    <path id="sm0" d="M253.963 284C244.611 284 237 278.393 237 271.5C237 264.607 244.611 259 253.963 259C263.315 259 270.926 264.607 270.926 271.524C270.926 278.442 263.315 284 253.963 284Z" fill="black"/>
    <path id="sm1" d="M253.963 261.855C248.861 261.855 244.382 263.717 241.904 266.499H266.023C263.545 263.717 259.065 261.855 253.963 261.855Z" fill="white"/>

    <path id="sam0" d="M251.108 259C266.955 259 280.794 268.103 281 268.242L279.814 270C279.514 269.799 249.658 250.192 228.453 269.898L227 268.349C234.543 261.335 243.083 259 251.108 259Z" fill="black"/>

    <path id="sam1" d="M217.001 255.499C217.001 257.489 216.211 259.396 214.804 260.803C213.398 262.21 211.49 263 209.501 263C207.511 263 205.604 262.21 204.197 260.803C202.79 259.396 202 257.489 202 255.499C202 251.357 209.501 243 209.501 243C209.501 243 217.001 251.357 217.001 255.499Z" fill="white"/>


    <defs>
    <clipPath id="clip0">
    <rect width="54" height="6" fill="white" transform="translate(227 259)"/>
    </clipPath>
    </defs>
    </svg>
        </h1>
        <video id="localVideo" autoplay muted></video>
        <!-- <video id="remoteVideo" autoplay muted></video> !-->
      </div>

</template>

<script>
import io from 'socket.io-client';
import TimelineMax from '../Tween.js';
import { gsap } from "gsap";
var socket = io.connect("http://localhost:5000/lips");


export default {
  name: 'Child',
  props: {
    msg: String
  },

  methods: {
     playSound (sound) {
      if(sound) {
        var audio = new Audio(sound);
        audio.play();
      }
    },

    emotion_recreation(){
      const emotion = ['angry', 'surprised'];
      const random = Math.floor(Math.random() * emotion.length);

      console.log(random);

      switch(emotion[random]){
        case 'angry':
          this.emotion_angry();
          break;
        
        case 'surprised':
          this.emotion_surprised();
          break;
      };
      
      
    },
    
    mouth_shape(){

    },
    
    emotion_angry(){
      const tl = new TimelineLite();
      tl
      .add("angery","+=0.55")
      .to("#nero", 0.3, {morphSVG:"#aero" },"angery")
      .to("#neri", 0.3, {morphSVG:"#aeri"},"angery")
      .to("#nelo", 0.3, {morphSVG:"#aelo"},"angery")
      .to("#neli", 0.3, {morphSVG:"#aeli"},"angery")
      .to("#nm", 0.3, {morphSVG:"#am"},"angery")
    },

    emotion_surprised(){
      const tl = new TimelineLite();
      tl
      .add("supperise","+=0.55")
      .to("#nero", 0.3, {morphSVG:"#sero"}, "supperise")
      .to("#neri", 0.3, {morphSVG:"#seri"}, "supperise")
      .to("#nelo", 0.3, {morphSVG:"#selo"}, "supperise")
      .to("#neli", 0.3, {morphSVG:"#seli"}, "supperise")
      .to("#nm", 0.3, {morphSVG:"#sm0"},"supperise")
      .to("#nm", 0.0, {morphSVG:"#sm1"},"supperise")
    },

    emotion_sad(){
      const tl = new TimelineLite();
      tl
      .add("sad","+=0.55")
      .to("#nero", 0.3, {morphSVG:"#saero"}, "sad")
      .to("#neri", 0.3, {morphSVG:"#saeri"}, "sad")
      .to("#nelo", 0.3, {morphSVG:"#saelo"}, "sad")
      .to("#neli", 0.3, {morphSVG:"#saeli"}, "sad")
      .to("#nm", 0.3, {morphSVG:"#sam0"},"sad")
      .to("#nm", 0.0, {morphSVG:"#sam1"},"sad")
    },

    
    createSubtitle(syncData, subtitles)
            {
                var element;
                for (var i = 0; i < syncData.length; i++) {
                    element = document.createElement('span');
                    element.setAttribute("id", "c_" + i);
                    element.innerText = syncData[i].value + " ";
                    subtitles.appendChild(element);
                }
            },

    syncAudioText() {
            var audioPlayer = document.getElementById("audiofile");
            var subtitles = document.getElementById("subtitles");
            var syncData = this.mouthCues;
            this.createSubtitle(syncData, subtitles);
            
            audioPlayer.addEventListener("timeupdate", function(e){
                syncData.forEach(function(element, index, array){
                    if( audioPlayer.currentTime >= element.start && audioPlayer.currentTime <= element.end )
                        subtitles.children[index].style.background = 'yellow';
                });
            });
        },


    
  },
  mounted() {
      let anime = document.createElement('script')
      anime.setAttribute('src', 'https://bot.takinweb.com/download/js/anime.js')
      document.head.appendChild(anime)
      /*
      let s_anime = document.createElement('script')
      //s_anime.setAttribute('src', 'https://bot.takinweb.com/download/js/script-anime.js')
      s_anime.setAttribute('src', 'http://localhost:8000/src/assets/js/script-anime.js')
      document.head.appendChild(s_anime)

      let selector = document.createElement('script')
      selector.setAttribute('src', 'https://bot.takinweb.com/download/js/selector.js')
      document.head.appendChild(selector)*/


    socket.on('send_json', msg => {
      var response = JSON.parse(msg);
      this.metadata = response.metadata;
      this.mouthCues = response.mouthCues;
      //localStorage.setItem('test', response.metadata['soundFile']);
      //var a = localStorage.getItem('test')
      //this.playSound();
    });

    socket.on('send_audio', msg => {
      const blob = new Blob([msg], { type: "audio/wav" });
      this.linkAudio = window.URL.createObjectURL(blob);
      //this.syncAudioText()
      //this.playSound(linkAudio)
      
    });
      
    },
  
data() {
   return {
    mouthCues:null,
    metadata:null,
    linkAudio: null,
    tl1: null,
   }
  },
  created() {
    socket.on('connect', function() {
      socket.emit('send_file', {data: 'connected!!!!!!!!!!!'});
    });
    //this.sizeAll();
    //this.tl1 = new TimelineMax({paused:true, onComplete: function() {$("masterControl").html("action");} });
    
    //this.sizeAll();


  },
}
</script>


<style scoped>
.circle { 
      width: 70vh; 
      height: 70vh; 
      background: white; 
      border-radius: 50%;
      margin: 0px auto;
      }
video {
  visibility: hidden;
}

#aelo, #aeli, #aero, #aeri{
  visibility:hidden;
  opacity: 0;
}

#selo, #seli, #sero, #seri{
  visibility:hidden;
  opacity: 0;
}

#saelo, #saeli, #saero, #saeri{
  visibility:hidden;
  opacity: 0;
}

#am, #sm0, #sm1, #sam0, #sam1{
  visibility:hidden;
  opacity: 0;
}

#controls {
	width:100%;
	padding: 20px 0;
	position: absolute;
	left:0;
	z-index: 102;
}

button {
	/*padding: 16px 30px;*/
	cursor: pointer;
	font-family: 'Source Sans Pro', sans-serif;
	font-weight: 700;
	font-size: 30px;
}

#titleBox {
	width:100%;
	padding: 20px 0;
	/*background: #262626;*/
	color:white;
	text-align:center;
	position: absolute;
	top:0;
	left:0;
	z-index: 101;
}

h1, p {
	font-family: 'Source Sans Pro', sans-serif;
	font-weight: 700;
	margin:0;
	padding: 0;
	line-height:1.2;
}

h1 {
	font-size: 2.5em;
}

h1, p span {
	color: #88ce02;
}

a {
  color: #fff;}
</style>

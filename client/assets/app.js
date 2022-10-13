const app = Vue.createApp({
    data() {
      return {
        appName: "Poor Man's Twitter",
        baseUrl: "http://127.0.0.1:8000/",
        tweetUrl: "api/tweet/tweets/",
        fields: ['name', 'content', 'created'],
        tweet: { name: "", content: ""},
        currentSort:'name',
        currentSortDir:'asc',
        tweetsList: [],
      };
    },
    methods: {
      sort:function(s) {
        if(s === this.currentSort) {
          this.currentSortDir = this.currentSortDir==='asc'?'desc':'asc';
        }
        this.currentSort = s;
      },
      async addTweet() {
        if (this.tweet.name == "") {
            alert("Enter tweet name and try again");
            return;
          }
          if (this.tweet.content == "") {
              alert("Enter tweet content and try again");
              return;
          }
        const requestBody = {
            name: this.tweet.name,
            content: this.tweet.content,
        };
        const res = await fetch(`${this.baseUrl}${this.tweetUrl}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });
        if (res) {
            const result = await res.json();
            this.fetchTweets();
            alert(result.message);
        }
      },
      async fetchTweets() {
        const res = await fetch(`${this.baseUrl}${this.tweetUrl}`, {
            mode: "cors"
        });
        if (res) {
            const result = await res.json();
            this.tweetsList = (result.data);
        }
      },

    },
    computed:{
      sortedTweetsList:function() {
        return this.tweetsList.sort((a,b) => {
          let modifier = 1;
          if(this.currentSortDir === 'desc') modifier = -1;
          if(a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
          if(a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
          return 0;
        });
      }
    },
    mounted: function() {
        this.fetchTweets();
    }
  });
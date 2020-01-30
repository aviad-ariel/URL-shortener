# URL-shortener

A URL shortener for dealing with long links, Built with Flask and Vue.JS.
Each URL gets a unique id, the id number is converted to base62 and that is the new shorter URL (example.com/id-in-base62)

#### State feature:
Provide some basic state about the app in the following format:
<pre><code>
  "failed_day":Int, #Number of failed redirections in the last day
  "failed_hour":Int, #Number of failed redirections in the last hour
  "failed_minute":Int, #Number of failed redirections in the last minute
  "success_day":Int, #Number of success redirections in the last day
  "success_hour":Int, #Number of success redirections in the last hour
  "success_minute":Int #Number of success redirections in the last minute
</code></pre>
The state can be accses at /stats endpoint

#### Usage:
clone the repository and cd into it
<pre><code>
  pip install
  python app.py
</code></pre>

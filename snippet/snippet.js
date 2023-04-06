// 20230404

/* Import -- WIP */
/*
//import mustcache from 'https://cdnjs.cloudflare.com/ajax/libs/mustache.js/0.7.2/mustache.min.js';

import showdown from 'https://cdnjs.cloudflare.com/ajax/libs/showdown/2.0.3/showdown.min.js';

//https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.css" rel="stylesheet" />
import prismCore from 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js';
  
import prismLoader from 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js';
*/

function fillHtmlToId(content, targetId) {
  document.getElementById(targetId).innerHTML = content;
}

function getTemplateById(templateId) {
  return document.getElementById(templateId).innerHTML;
}

/*
 snip - sinlge snippet
*/

// global
let snipConf = {};
let snippetjs = {
  log: function(data) {
    let e = document.getElementById("snipResult" + snipConf.activeSnipId)
    e.insertAdjacentHTML('beforeend', data + "<br/>");
  }
}

// Config
let tmplSearch = `
<div class="pb-4">
<input type="text" class="w-100" id="searchSnippetInput" onkeyup="searchSnippet()" placeholder="Search for snippet..">
</div>
`

// class "snipDiv" - for search
let tmplSnippet = `
<div class="row row-cols-1 row-cols-lg-2 row-cols-xxl-3 g-4">
{{#snippets}}
  <div class="col snipDiv" data-id="{{snip_id}}">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
        {{#tags}}
        <small class="d-inline-flex mb-3 px-2 py-1 fw-semibold text-success bg-success bg-opacity-10 border border-success border-opacity-10 rounded-2">{{tags}}</small>
        {{/ tags}}
        </h5>
        <p class="card-text">
        {{#content}}
        {{{content}}}
        {{/content}}        

        {{#code}}
        <pre><code class="language-{{syntax}}">{{code}}</code></pre>        
        {{#snip_run}}
        <button onclick="runScript( {{snip_id}} )">run</button>
        <pre id="snipResult{{snip_id}}"></pre>
        {{/snip_run}}
        {{/code}}

        {{#codeUrl}}
        <pre><code class="language-{{syntax}}" data-url="{{codeUrl}}"></code></pre>   
        <button class='showCode' onclick="showCode( {{snip_id}} )">show</button>
        {{/codeUrl}}
        
        </p>
      </div>          
    </div>
  </div>
{{/snippets}}    
</div >
`

function snipDefaultConf() {
  let snipConf = {
    // internal
    snipId: 0,
    repositoryCode: {}
  }

  return snipConf;
}


// Main Function
function snippet(snippets, conf) {

  // initialize
  let defaultConf = snipDefaultConf();
  snipConf = {
    ...defaultConf,
    ...conf
  };
  initSnippets(snippets, snipConf);

  snipConf.snippets = snippets; // assign to global

  var data = { // wrap by object "data" for mustcahe
    snippets: snippets
  }

  //console.log("snippet", data.snippets)
  var html = "";
  html = Mustache.to_html(tmplSnippet, data);

  html = tmplSearch + html; // append "Search"

  fillHtmlToId(html, "snippet");
}


function initSnippets(snippets, conf) {

  var converter = new showdown.Converter(
    { disableForced4SpacesIndentedSublists: true }
  ); // markdown

  // prefix "snip_"
  snippets.forEach(snip => {

    snip.snip_id = conf.snipId;


    if (snip.content) {
      html = converter.makeHtml(snip.content);
      snip.content = html; // note:  {{{unescape}}} the field in template
    }


    if (snip.output && snip.output == "js") {

      snip.snip_run = true;

      var fx = null;
      eval("fx = function() { " + snip.code + "}; ");
      conf.repositoryCode[conf.snipId] = fx;
    }
    conf.snipId++;
  });
}

function filterSnippet(filter, id) {
  //console.log( "title", snipConf.snippets[id].title );  

  // title
  if (snipConf.snippets[id].title.toLowerCase().indexOf(filter) > -1)
    return true;

  // tags
  if (snipConf.snippets[id].tags) {
    if (snipConf.snippets[id].tags.find(
      t => { return t.toLowerCase().indexOf(filter) > -1 })
    ) return true
  }

  return false;
}

function searchSnippet() { // v1: Search Title only

  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('searchSnippetInput');

  filter = input.value.toLowerCase();
  //console.log("input", filter);

  let snipDiv = document.querySelectorAll(".snipDiv");

  //console.group('search:', filter);
  //console.log("snipDiv.length", snipDiv.length);

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < snipDiv.length; i++) {
    id = snipDiv[i].dataset.id;
    if (filterSnippet(filter, id)) {
      snipDiv[i].style.display = "";
    } else {
      snipDiv[i].style.display = "none";
    }
  }
  //console.groupEnd();

}
// fire "run"
function runScript(snippetId) {
  snipConf.activeSnipId = snippetId;
  snipConf.repositoryCode[snippetId](); // 
}

// fire "show" for codeUrl
function showCode(snippetId) {
  let snipDivCode = document.querySelectorAll("[data-id='" + snippetId + "'] code[data-url]");
  if (snipDivCode.length == 0) return;

  console.log(snipDivCode[0].dataset.url);
  codeDev = snipDivCode[0];
  fetch(codeDev.dataset.url)
    .then(res => res.text())
    .then(data => {
      codeDev.appendChild(document.createTextNode(data))

      // highlight
      Prism.highlightElement(codeDev);

      // hide button
      let snipDivBtn = document.querySelectorAll("[data-id='" + snippetId + "'] button.showCode");
      for (let i of snipDivBtn) {
        i.style.display = "none";
      }
    });

}



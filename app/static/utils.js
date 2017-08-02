function reload(sel) {
  location.reload();
}

/**
 * Get the value of a querystring
 * @param  {String} field The field to get the value of
 * @param  {String} url   The URL to get the value from (optional)
 * @return {String}       The field value
 */
var getQueryString = function ( field, url ) {
    var href = url ? url : window.location.href;
    var reg = new RegExp( '[?&]' + field + '=([^&#]*)', 'i' );
    var string = reg.exec(href);
    return string ? string[1] : null;
};


function queryString() {
  var urlParams = new URLSearchParams(window.location.search);
  console.log(urlParams.get('year'));
}


function queryString2() {
  document.getElementById("demo").innerHTML = 'test' + window.location.search;
  console.log(window.location.search);
}

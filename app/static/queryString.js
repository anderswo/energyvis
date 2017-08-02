// Check for Query String
var urlParams = new URLSearchParams(window.location.search);

if (urlParams.get('year') == null) {
  window.location.href += "?geo=EU28&year=2015";
}

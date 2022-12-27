
//Build Tabulator
var table = new Tabulator("#example-table", {
    ajaxURL: "/api/data",
    height:"311px",
    layout:"fitColumns",
    selectable:true,
    placeholder:"No Data Set",
    columns:[
        {title:"id", field:"0", sorter:"string", width:200},
        {title:"Purchaser", field:"1", sorter:"string", width:200},
        {title:"Purchase Order Number", field:"2", sorter:"string", width:200},
        {title:"Supplier", field:"3", sorter:"string"},
        {title:"Part Number", field:"4", sorter:"string"},
        {title:"Part Description", field:"5", formatter:"star", hozAlign:"center", width:100},
        {title:"Quantity", field:"6", sorter:"string", editor:"input"},
        {title:"Part Price", field:"7", sorter:"date", hozAlign:"center"},
        {title:"Total Cost", field:"8", sorter:"string"},
        {title:"Delete Row", field:"9", hozAlign:"center", formatter:"tickCross", sorter:"boolean"},
        //column definition in the columns array
        //{formatter:"buttonCross", width:40, align:"center", cellClick:function(e, cell){
        //    cell.getRow().delete()}},
        {formatter:"buttonCross", width:40, align:"center", cellClick:function(e, cell){
        //e - the click event object
        //cell - cell component
        doit(e,cell);
    },},
    ],
});
columns: ['', '', '', '', '', '', '', '', '']
/*

cellClick:function(e, cell){
        //e - the click event object
        //cell - cell component
    },



var table = new Tabulator("#example-table", {
    ajaxURL:"http://www.getmydata.com/now", //ajax URL
});

//trigger AJAX load on "Load Data via AJAX" button click
document.getElementById("ajax-trigger").addEventListener("click", function(){
    table.setData("/api/data");
});

*/

function doit(e, cell) {
    debugger;
    var row = cell.getRow();
    var rowData = row.getData();
    alert("purchase OrderId is: " + rowData["0"]) //id in purchaserOrder table
    id = rowData["0"]
    //var row = table.getSelectedData(); //get array of currently selected data.
    //var cell = row.getCell("1");
    //var cellValue = cell.getValue();
    //alert("orderid: " + cellvalue)
    cell.getRow().delete();
    console.log("delete row done");
    alert("delete row");

    table.setData("/api/data/" + id);



}
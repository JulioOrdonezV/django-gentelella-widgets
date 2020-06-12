$(document).ready(function() {
    $('.data-table').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": "datatable/data"
    } );
} );
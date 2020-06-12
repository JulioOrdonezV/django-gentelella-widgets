$(document).ready(function() {
    $('.data-table').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": "data",
        "columns": [
            { "data": "name" },
            { "data": "num_children" },
            { "data": "country" }
        ]
    } );
} );
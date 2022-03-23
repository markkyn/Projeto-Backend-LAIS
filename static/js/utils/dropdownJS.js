$('#id_estabelecimento_Field').change(function() {
    var url = $('#agendamentoForm_id').attr("horarios-data");
    var estabelecimento_name = $(this).val();

    $.ajax({
        url: url,
        data: {
            "estabelecimento": estabelecimento_name
        },
        success: function(data) {
            $('#id_horario_Field').html(data);

            console.log("Carregou essa função")

        }
    });

});
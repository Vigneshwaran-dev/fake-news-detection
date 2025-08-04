$(document).ready(function() {
    $('#newsForm').submit(function(e) {
        e.preventDefault();
        const text = $('#newsText').val().trim();
        if (!text) return;
        
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: { text: text },
            success: function(response) {
                if (response.error) {
                    alert(response.error);
                    return;
                }
                $('#realPercent').text(Math.round(response.real_prob * 100) + '%');
                $('#fakePercent').text(Math.round(response.fake_prob * 100) + '%');
                $('#realProgress').css('width', (response.real_prob * 100) + '%');
                $('#fakeProgress').css('width', (response.fake_prob * 100) + '%');
                const verdictEl = $('#verdictText');
                verdictEl.text(response.verdict);
                $('#verdictAlert').removeClass('alert-success alert-danger')
                    .addClass(response.verdict === 'REAL NEWS' ? 'alert-success' : 'alert-danger');
                $('#resultCard').show();
            },
            error: function() {
                alert('Error processing your request');
            }
        });
    });
});

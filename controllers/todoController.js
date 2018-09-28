module.exports = function(app) {
    app.get('/todo', (req, res) => {
        res.send('hi');
    });
    
    app.post('/todo', (req, res) => {

    });
    
    app.delete('/todo', (req, res) => {

    });
};

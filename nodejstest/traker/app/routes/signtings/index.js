import Route from '@ember/routing/route';

export default Route.extend({
  model(){
    return [
      {id:1, location:'tianjin', signtedAt: new Date('2019-03-07')},
      {id:2, location:'beijing', signtedAt: new Date('2019-03-08')},
      {id:3, location:'henan', signtedAt: new Date('2019-03-09')},
      {id:4, location:'hunan', signtedAt: new Date('2019-03-10')}
    ]
  }
});

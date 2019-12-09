import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | signtings/new', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:signtings/new');
    assert.ok(route);
  });
});

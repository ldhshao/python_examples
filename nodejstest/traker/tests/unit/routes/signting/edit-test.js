import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | signting/edit', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:signting/edit');
    assert.ok(route);
  });
});

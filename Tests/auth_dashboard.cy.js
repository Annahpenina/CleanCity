describe('CleanCity App - Auth to Dashboard Flow', () => {
  it('should log in and navigate to dashboard successfully', () => {
    cy.visit('https://cleancityqa.netlify.app/');


    cy.get('#auth-links a[data-page="login"]').click();

    cy.get('#login-page').should('be.visible');
    cy.get('#login-email').type('user@cleancity.com');
    cy.get('#login-password').type('password123');
    cy.get('#login-form').submit();

    cy.get('#dashboard-page', { timeout: 10000 }).should('be.visible');
    cy.get('#requests-table').should('exist');
  });
});

export default {
  async fetch(req) {
    const url = new URL(req.url);
    if (url.pathname.startsWith('/switch/')) {
      // TODO: call controlplane routing API and redirect to correct region
      return Response.redirect('https://uk.rmy.app', 302);
    }
    return new Response('RMY edge alive', { status: 200 });
  }
}

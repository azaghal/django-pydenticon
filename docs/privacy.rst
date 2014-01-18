.. _privacy:

Privacy
=======

Generating identicons thorugh Django Pydenticon using raw user data may have
undesirable consequences on privacy if the data used is meant to be ketp as
a secret.

This privacy issue can in particular arise if using data like usernames,
e-mails, or real names of users for generating avatars in publicly-accessible
websites.

As a rule-of-thumb, you should **never**, **ever** pass such data raw into the
identicon URL. This approach would leak the confidential information in plain
text to any interested parties. Instead, calculate a digest of the raw data, and
pass the hex digest as part of the URL instead.

.. note::
   In some cases you may opt to pass raw data. For example, if usernames are
   visible as part of posted comments, they're probably already scrapeable, and
   having them as part of identicon URL won't hide them anyway.

Additionally, the default digest algorithm (*MD5*) may not be safe enough for
such data. Even in case where a stronger digest algorithm is used, an attacker
might attempt to generate `rainbow tables
<https://en.wikipedia.org/wiki/Rainbow_tables>`_, and scrape the web pages
hashed data contained within identicon URLs.

There's two feasible approaches to resolve this:

* Always apply *salt* to user-identifiable data before calculating a hex
  digest. This can hugely reduce the efficiency of brute force attacks based on
  rainbow tables (although it will not mitigate it completely).
* Instead of hashing the user-identifiable data itself, every time you need to
  do so, create some random data instead, hash that random data, and store it
  for future use (cache it), linking it to the original data that it was
  generated for. This way the hex digest being put as part of an image link into
  HTML pages is not derived in any way from the original data, and can therefore
  not be used to reveal what the original data was.

Keep in mind that using identicons will inevitably still allow people to track
someone's posts across your website. Identicons will effectively automatically
create pseudonyms for people posting on your website. If that may pose a
problem, it might be better not to use identicons at all.

Finally, small summary of the points explained above:

* Always use hex digests in identicon URLs.
* Instead of using privately identifiable data for generating the hex digest,
  use randmoly generated data, and associate it with privately identifiable
  data. This way hex digest cannot be traced back to the original data through
  brute force or rainbow tables.
* If unwilling to generate and store random data, at least make sure to use
  salt when hashing privately identifiable data.

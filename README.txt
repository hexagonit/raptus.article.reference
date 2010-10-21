Introduction
============

You have a site where you would like to list some internal or external references but you are
not able to present them in a nice way. With raptus.article.reference you can do it. 

The following features for raptus.article are provided by this package:

Fields
------
    * Provides support for internal or external references on nested articles

Dependencies
------------
    * archetypes.schemaextender
    * raptus.article.nesting

Installation
============

To install raptus.article.reference into your Plone instance, locate the file
buildout.cfg in the root of your Plone instance directory on the file system,
and open it in a text editor.

Add the actual raptus.article.reference add-on to the "eggs" section of
buildout.cfg. Look for the section that looks like this::

    eggs =
        Plone

This section might have additional lines if you have other add-ons already
installed. Just add the raptus.article.reference on a separate line, like this::

    eggs =
        Plone
        raptus.article.reference

Note that you have to run buildout like this::

    $ bin/buildout

Then go to the "Add-ons" control panel in Plone as an administrator, and
install or reinstall the "raptus.article.default" product.

Note that if you do not use the raptus.article.default package you have to
include the zcml of raptus.article.reference either by adding it
to the zcml list in your buildout or by including it in another package's
configure.zcml.

Usage
=====

Edit an article which is contained in another. You will now have the new options 
"Internal reference" and "External reference" in your tab "settings". Add your 
reference press "save". The link on the specific article displayed by the components
listing sub articles now refers to the specified reference. The following packages
provide components respecting the reference setting:

    * `raptus.article.listings <http://pypi.python.org/pypi/raptus.article.listings>`_
    * `raptus.article.contentfader <http://pypi.python.org/pypi/raptus.article.contentfader>`_
    * `raptus.article.contentflow <http://pypi.python.org/pypi/raptus.article.contentflow>`_
    * `raptus.article.randomcontent <http://pypi.python.org/pypi/raptus.article.randomcontent>`_

Copyright and credits
=====================

raptus.article is copyrighted by `Raptus AG <http://raptus.com>`_ and licensed under the GPL. 
See LICENSE.txt for details.

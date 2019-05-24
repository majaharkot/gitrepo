<!doctype html>
<html lang="pl">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="To byłam ja :)">
    <title><?php get_page_clean_title(); ?> &lt; <?php get_site_name(); ?></title>

    <!-- Bootstrap core CSS -->
    <link href="<?php get_theme_url(); ?>/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="<?php get_theme_url(); ?>/style.css" rel="stylesheet">
    <?php get_header(); ?>
  </head>
  <body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <a class="navbar-brand" href="<?php get_site_url(); ?>"><?php get_site_name(); ?></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mx-auto">
          <?php get_navigation(return_page_slug()); ?>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Szukaj" aria-label="Szukaj">
          <button class="btn btn-secondary my-2 my-sm-0" type="submit">Szukaj</button>
        </form>
      </div>
    </nav>

    <main role="main" class="container">
      <div class="row">
        <div class="col-sm-8">
          <h1><?php get_page_title(); ?></h1>
          <?php get_page_content(); ?>
        </div>
        <div class="col-sm-4">
          <?php get_component('sidebar'); ?>
        </div>
      </div>
    </main><!-- /.container -->

    <div class="container">
      <?php get_footer(); ?>
    </div>
    <script src="<?php get_theme_url(); ?>/js/jquery.min.js"></script>
    <script src="<?php get_theme_url(); ?>/js/popper.min.js"></script>
    <script src="?php get_theme_url(); ?>/js/bootstrap.min.js"></script>

  </body>
</html>

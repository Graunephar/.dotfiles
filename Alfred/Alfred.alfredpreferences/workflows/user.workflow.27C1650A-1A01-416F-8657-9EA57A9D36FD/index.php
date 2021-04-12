#!/usr/bin/php
<?php
/**
 * @author Sellim Dauti (Phantombox)
 * @link https://phantom-box.com
 */

$queryParams = explode(',', $argv[1]);

$xSize = null;
$ySize = null;
$imageType = 'jpg';
$text = '';

$availableImageTypes = [
  'png',
  'jpg',
  'gif',
];

foreach ($queryParams as $queryParam) {
  if (is_numeric($queryParam)) {
    if ($xSize === null) {
      $xSize = $queryParam;
      continue;
    }
    else {
      $ySize = $queryParam;
      continue;
    }
  }

  if (in_array($queryParam, $availableImageTypes)) {
    $imageType = $queryParam;
    continue;
  }

  $text = $queryParam;
}

if ($xSize === null) {
  echo '';
  return;
}

if ($ySize === null) {
  $ySize = $xSize;
}

if (in_array($queryParams[2], $availableImageTypes)) {
  $imageType = $queryParams[2];
}

$placeholderUriBuildService = new PlaceholderUriBuildService();
echo $placeholderUriBuildService->buildUri($xSize, $ySize, $imageType, $text);

class PlaceholderUriBuildService {

  const URI = 'https://via.placeholder.com';

  public function buildUri(int $x, int $y, string $imageType, $text)
  {
    $placeholderImageUri = sprintf(self::URI . '/%sx%s.%s', $x, $y, $imageType);

    if ($text === '') {
      return $placeholderImageUri;
    }

    return $placeholderImageUri . '?text=' . $text;
  }
}

<script>
	import { onMount } from 'svelte';
	let songs;
	let timer;
	let statusMsg = 'Try searching for songs';
	const apiServer = 'http://192.168.1.11:4444';
	let isTopOfPage = false;

	const setTopOfPage = () => {
		isTopOfPage = !isTopOfPage;
	};

	const qeueSong = async (videoId) => {
		await fetch('http://play.local:420/https://www.youtube.com/watch?v=' + videoId);
	};

	const debounce = (v) => {
		clearTimeout(timer);
		timer = setTimeout(async () => {
			if (v === '') {
				statusMsg = 'No songs searched';
				songs = undefined;
			} else {
				statusMsg = 'Searching Songs';
			}
			const response = await fetch(apiServer + '/music/songs/' + v);
			const data = await response.json();
			songs = getSongs(data);
			console.log(songs);
		}, 1000);
	};

	const getSongs = (songListData) => {
		const songList = songListData.filter((song) => song.resultType === 'song');
		return songList;
	};

	const getMaxImageSizeURL = (song) => {
		let imageLenght = song.thumbnails.slice(-1);
		return imageLenght[0].url;
	};

	// onMount(async () => {
	// 	const response = await fetch('http://127.0.0.1:4231/music/Three');
	// 	const data = await response.json();
	// 	songs = getSongs(data);
	// });
</script>

<div />
<header class:not-top={isTopOfPage === true}>
	<img class="logo-img" src="/logo.png" alt="" />
	<h1>Mewso Player</h1>
	<input
		type="search"
		name=""
		id=""
		placeholder="Search Song"
		on:keyup={({ target: { value } }) => debounce(value)}
	/>
</header>
<div class="main">
	{#if songs == undefined}
		<p>
			{statusMsg}
		</p>
		{#if statusMsg == 'Searching Songs'}
			<img src="/load.gif" alt="loading" />
		{/if}
	{:else}
		<div class="songs">
			{#each songs as song}
				<section class="song">
					<img
						loading="lazy"
						src={getMaxImageSizeURL(song) ? getMaxImageSizeURL(song) : 'hello'}
						alt={song.title}
					/>
					<p class="song-title">{song.title}</p>
					<p class="song-artist">
						<a href="/artist/{song.artists[0].id}">{song.artists[0].name}</a>
					</p>
					<p class="song-length">{song.duration}</p>
					<button on:click|once={() => qeueSong(song.videoId)}>
						<svg
							class="qeue-icon"
							xmlns="http://www.w3.org/2000/svg"
							xmlns:xlink="http://www.w3.org/1999/xlink"
							aria-hidden="true"
							role="img"
							preserveAspectRatio="xMidYMid meet"
							viewBox="0 0 24 24"
							><path
								d="M3 6c-.55 0-1 .45-1 1v13c0 1.1.9 2 2 2h13c.55 0 1-.45 1-1s-.45-1-1-1H5c-.55 0-1-.45-1-1V7c0-.55-.45-1-1-1zm17-4H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 9h-3v3c0 .55-.45 1-1 1s-1-.45-1-1v-3h-3c-.55 0-1-.45-1-1s.45-1 1-1h3V6c0-.55.45-1 1-1s1 .45 1 1v3h3c.55 0 1 .45 1 1s-.45 1-1 1z"
								fill="currentColor"
							/></svg
						>
					</button>
					<div class="corner-wrapper">
						<iframe
							width="180"
							height="80"
							src="https://www.youtube.com/embed/{song.videoId}"
							title="YouTube video player"
							frameborder="0"
							allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
							allowfullscreen
						/>
					</div>
				</section>
			{/each}
		</div>
	{/if}
</div>

<style>
	.qeue-icon {
		width: 37px;
		height: 37px;
	}
	.not-top {
		background: red;
	}

	.corner-wrapper {
		display: block;
		overflow: hidden;
		width: 180px;
		height: 80px;
		border-top-right-radius: 7px;
		border-bottom-right-radius: 7px;
		transform: translateZ(0px);
	}
	header {
		font-family: 'Roboto', sans-serif;
		display: grid;
		justify-items: center;
		position: sticky;
		top: 0;
		background: rgba(255, 255, 255, 0.2);
		backdrop-filter: blur(8px);
		-webkit-backdrop-filter: blur(8px);
		width: 100%;
		z-index: 99;
	}
	.logo-img {
		width: 90px;
		margin-top: 1rem;
	}
	input {
		padding: 1rem;
		margin-bottom: 1rem;
		width: 93%;
		max-width: 600px;
		font-family: 'Roboto', sans-serif;
	}
	.main {
		width: 90%;
		max-width: 1400px;
		margin: 0 auto;
		display: grid;
		justify-items: center;
	}
	h1 {
		font-size: 32px;
		font-family: 'Roboto', sans-serif;
	}
	h3 {
		font-size: 21px;
		font-family: 'Roboto', sans-serif;
	}
	.songs {
		display: grid;
		width: 100%;
		justify-content: center;
		gap: 1rem;
		padding-bottom: 3rem;
	}
	.song {
		gap: 1rem;
		font-family: 'Roboto', sans-serif;
		display: grid;
		grid-template-columns: auto 1fr auto auto auto 180px;
		box-shadow: 6px 10px 16px 4px rgba(0, 0, 0, 0.14);
		border-radius: 7px;
		background-color: white;
		font-weight: 700;
		align-items: center;
	}
	.song img {
		border-top-left-radius: 7px;
		border-bottom-left-radius: 7px;
		width: 80px;
	}

	p {
		font-family: 'Roboto', sans-serif;
	}

	button {
		background: transparent;
		border: none;
	}
	button:hover {
		cursor: pointer;
		transform: scale(1.1);
	}

	.song-artist a:visited,
	.song-artist a,
	.song-length {
		color: gray;
		text-decoration: none;
	}

	@media only screen and (max-width: 800px) {
		.song {
			grid-template-columns: auto 1fr auto auto 180px;
		}
		.song-length {
			display: none;
		}
	}
	@media only screen and (max-width: 700px) {
		.song {
			grid-template-columns: auto 1fr auto 180px;
		}
		.song-artist {
			display: none;
		}
	}
	@media only screen and (max-width: 600px) {
		.song {
			grid-template-columns: auto 1fr auto;
		}
		.corner-wrapper {
			display: none;
		}
		.qeue-icon {
			padding-right: 1rem;
		}
	}
</style>
